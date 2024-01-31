from module.umamusume.context import *
from module.umamusume.script.cultivate_task.support_card import get_support_card_score
import numpy as np

log = logger.get_logger(__name__)


def get_operation(ctx: UmamusumeContext) -> TurnOperation | None:
    turn_operation = TurnOperation()
    if not ctx.cultivate_detail.debut_race_win:
        turn_operation.turn_operation_type = TurnOperationType.TURN_OPERATION_TYPE_RACE

    attribute_result = get_training_basic_attribute_score(ctx, ctx.cultivate_detail.turn_info,
                                                          ctx.cultivate_detail.expect_attribute)
    support_card_result = get_training_support_card_score(ctx)
    training_level_result = get_training_level_score(ctx)

    attribute_result_max = np.max(attribute_result)
    attribute_result_min = np.min(attribute_result)
    normalized_attribute_result = (attribute_result - attribute_result_min) / (
            attribute_result_max - attribute_result_min)

    support_card_max = np.max(support_card_result)
    support_card_min = np.min(support_card_result)
    if support_card_max != support_card_min:
        normalized_support_card_result = (support_card_result - support_card_min) / (
                support_card_max - support_card_min)
    else:
        normalized_support_card_result = [1, 1, 1, 1, 1]

    training_level_max = np.max(training_level_result)
    training_level_min = np.min(training_level_result)
    if training_level_min != training_level_max:
        normalized_training_level_result = (training_level_result - training_level_min) / (
                training_level_max - training_level_min)
    else:
        normalized_training_level_result = [1, 1, 1, 1, 1]

    # 第一年
    if ctx.cultivate_detail.turn_info.date <= 24:
        attr_weight = 0.2
        support_card_weight = 0.6
        training_level_weight = 0.2
    # 第二年合宿前
    elif 25 < ctx.cultivate_detail.turn_info.date <= 36:
        attr_weight = 0.6
        support_card_weight = 0.2
        training_level_weight = 0.2
    # 第二年合宿期间
    elif 36 < ctx.cultivate_detail.turn_info.date <= 40:
        attr_weight = 0.8
        support_card_weight = 0.2
        training_level_weight = 0
    # 第二年合宿后至第三年前
    elif 40 < ctx.cultivate_detail.turn_info.date <= 48:
        attr_weight = 0.6
        support_card_weight = 0.2
        training_level_weight = 0.2
    # 第三年合宿前
    elif 48 < ctx.cultivate_detail.turn_info.date <= 60:
        attr_weight = 0.6
        support_card_weight = 0.1
        training_level_weight = 0.3
    # 第三年合宿期间
    elif 60 < ctx.cultivate_detail.turn_info.date <= 64:
        attr_weight = 1
        support_card_weight = 0
        training_level_weight = 0
    # 第三年至结束
    elif 64 < ctx.cultivate_detail.turn_info.date <= 99:
        attr_weight = 0.8
        support_card_weight = 0
        training_level_weight = 0.2
    else:
        attr_weight = 1
        support_card_weight = 0
        training_level_weight = 0

    # 训练得分
    training_score = []
    for i in range(5):
        training_score.append(normalized_attribute_result[i] * attr_weight + normalized_support_card_result[i] *
                              support_card_weight + normalized_training_level_result[i] * training_level_weight)
    log.debug("训练综合得分：" + str(training_score))

    # 出道战成功才能参加比赛
    if ctx.cultivate_detail.debut_race_win:
        extra_race_this_turn = [i for i in ctx.cultivate_detail.extra_race_list if str(i)[:2]
                                == str(ctx.cultivate_detail.turn_info.date)]
        if len(extra_race_this_turn) != 0:
            turn_operation.turn_operation_type = TurnOperationType.TURN_OPERATION_TYPE_RACE
            turn_operation.race_id = extra_race_this_turn[0]
            return turn_operation

    medic = False
    if ctx.cultivate_detail.turn_info.medic_room_available and ctx.cultivate_detail.turn_info.remain_stamina <= 65:
        medic = True

    trip = False
    if not ctx.cultivate_detail.turn_info.medic_room_available and (ctx.cultivate_detail.turn_info.date <= 36 and ctx.cultivate_detail.turn_info.motivation_level.value <= 3 and ctx.cultivate_detail.turn_info.remain_stamina < 90 and not support_card_max >= 3
                                                                    or 40 < ctx.cultivate_detail.turn_info.date <= 60 and ctx.cultivate_detail.turn_info.motivation_level.value <= 4 and ctx.cultivate_detail.turn_info.remain_stamina < 90
                                                                    or 64 < ctx.cultivate_detail.turn_info.date <= 99 and ctx.cultivate_detail.turn_info.motivation_level.value <= 4 and ctx.cultivate_detail.turn_info.remain_stamina < 90):
        trip = True

    rest = False
    if ctx.cultivate_detail.turn_info.remain_stamina <= 48:
        rest = True
    elif (
            ctx.cultivate_detail.turn_info.date == 36 or ctx.cultivate_detail.turn_info.date == 60) and ctx.cultivate_detail.turn_info.remain_stamina < 65:
        rest = True

    expect_operation_type = TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN

    if medic and expect_operation_type is TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN:
        expect_operation_type = TurnOperationType.TURN_OPERATION_TYPE_MEDIC

    if trip and expect_operation_type is TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN:
        expect_operation_type = TurnOperationType.TURN_OPERATION_TYPE_TRIP

    if rest and expect_operation_type is TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN:
        expect_operation_type = TurnOperationType.TURN_OPERATION_TYPE_REST

    if expect_operation_type is TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN:
        expect_operation_type = TurnOperationType.TURN_OPERATION_TYPE_TRAINING
        turn_operation.training_type = TrainingType(training_score.index(np.max(training_score)) + 1)

    if turn_operation.turn_operation_type != TurnOperationType.TURN_OPERATION_TYPE_UNKNOWN:
        turn_operation.turn_operation_type_replace = expect_operation_type
    else:
        turn_operation.turn_operation_type = expect_operation_type
    return turn_operation


def get_training_level_score(ctx: UmamusumeContext):
    expect_attribute = ctx.cultivate_detail.expect_attribute
    total_score = 2
    result = []
    for i in range(len(expect_attribute)):
        result.append(expect_attribute[i] / sum(expect_attribute) * total_score)
    log.debug("每个训练设施的得分：" + str(result))
    return result


def get_training_support_card_score(ctx: UmamusumeContext) -> list[float]:
    turn_info = ctx.cultivate_detail.turn_info
    result = []
    for i in range(len(turn_info.training_info_list)):
        score = 0
        for j in range(len(turn_info.training_info_list[i].support_card_info_list)):
            score += get_support_card_score(ctx, turn_info.training_info_list[i].support_card_info_list[j])
        result.append(score)
    log.debug("每个训练的支援卡得分：" + str(result))
    return result


def get_training_basic_attribute_score(ctx: UmamusumeContext, turn_info: TurnInfo, expect_attribute: list[int]) -> list[float]:
    date = turn_info.date
    cultivate_expect_attribute = expect_attribute.copy()
    extra_weight = [0, 0, 0, 0, 0]
    if len(ctx.cultivate_detail.extra_weight) == 3:
        if 0 < date <= 24:
            extra_weight = ctx.cultivate_detail.extra_weight[0]
        elif 24 < date <= 48:
            extra_weight = ctx.cultivate_detail.extra_weight[1]
        elif 48 < date:
            extra_weight = ctx.cultivate_detail.extra_weight[2]
    log.debug("本回合额外权重：" + str(extra_weight))
    turn_expect_attribute = [0, 0, 0, 0, 0]
    ura_extra_attr = 50
    if date > 72:
        ura_extra_attr = 0
        date = 72
    for i in range(len(cultivate_expect_attribute)):
        turn_expect_attribute_item = (int((cultivate_expect_attribute[i] - ura_extra_attr) * (date / 72))
                                      ) + 120 * (1 - date / 72)
        turn_expect_attribute_item = (1 + extra_weight[i]) * turn_expect_attribute_item
        if turn_expect_attribute_item > cultivate_expect_attribute[i]:
            turn_expect_attribute_item = cultivate_expect_attribute[i]
        turn_expect_attribute[i] = turn_expect_attribute_item if turn_expect_attribute_item > 0 else 1
    turn_uma_attr = [turn_info.uma_attribute.speed, turn_info.uma_attribute.stamina, turn_info.uma_attribute.power,
              turn_info.uma_attribute.will, turn_info.uma_attribute.intelligence]
    result = []
    expect_attribute_all_complete = all(x >= y for x, y in zip(turn_uma_attr, cultivate_expect_attribute))
    if expect_attribute_all_complete:
        log.debug("育成目标属性已达成")
        for i in range(len(turn_info.training_info_list)):
            incr = [turn_info.training_info_list[i].speed_incr, turn_info.training_info_list[i].stamina_incr,
                    turn_info.training_info_list[i].power_incr, turn_info.training_info_list[i].will_incr,
                    turn_info.training_info_list[i].intelligence_incr]
            rating_incr = 0
            for j in range(len(incr)):
                if incr[j] != 0:
                    rating_incr += incr[j]
            result.append(rating_incr)
    else:
        for i in range(len(turn_info.training_info_list)):
            incr = [turn_info.training_info_list[i].speed_incr, turn_info.training_info_list[i].stamina_incr,
                    turn_info.training_info_list[i].power_incr, turn_info.training_info_list[i].will_incr,
                    turn_info.training_info_list[i].intelligence_incr]
            rating_incr = 0
            for j in range(len(incr)):
                if incr[j] != 0 and turn_uma_attr[j] <= cultivate_expect_attribute[j]:
                    attr_difference = turn_expect_attribute[j] - turn_uma_attr[j]
                    # rating_incr += get_basic_status_score(incr[j] + turn_uma_attr[j]) - get_basic_status_score(turn_uma_attr[j])
                    if j == 3:
                        rating_incr += incr[j]
                    else:
                        if attr_difference >= incr[j]:
                            rating_incr += incr[j]
                        else:
                            if attr_difference < 0:
                                attr_difference = 0
                            rating_incr += attr_difference
                            overflow_incr = incr[j]-attr_difference
                            if cultivate_expect_attribute[j] - turn_expect_attribute[j] > overflow_incr:
                                rating_incr += 0.25 * overflow_incr
                            else:
                                rating_incr += 0.25 * (cultivate_expect_attribute[j] - turn_expect_attribute[j])
            # rating_incr += turn_info.training_info_list[i].skill_point_incr * 1.45
            result.append(rating_incr * (1 + extra_weight[i]))
        log.debug("每个训练的原始属性增长得分：" + str(result))
        log.debug("本回合预期属性：" + str(turn_expect_attribute))
        target_percent = [0, 0, 0, 0, 0]
        for i in range(len(turn_uma_attr)):
            target_percent[i] = turn_uma_attr[i] / turn_expect_attribute[i]
        avg = sum(target_percent) / len(target_percent)
        for i in range(len(result)):
            result[i] = result[i] * (1 - (target_percent[i] - avg))
    log.debug("每个训练的属性增长得分：" + str(result))
    return result


status_score = [0.66, 1.15, 1.71, 2.25, 2.7, 2.96, 3.2, 3.45, 4.01, 4.26, 5.36, 6.70]


def get_basic_status_score(status: int) -> float:
    result = 0
    for i in range(13):
        if status > 0:
            status -= 100
            result += status_score[i] * 100
        else:
            if i - 1 > 11:
                log.debug("识别错误")
                return 0
            result += status * status_score[i - 1]
            break
    return result


if __name__ == '__main__':
    print(str(get_basic_status_score(1169)))
