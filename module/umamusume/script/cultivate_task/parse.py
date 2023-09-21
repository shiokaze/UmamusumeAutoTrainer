import re
from difflib import SequenceMatcher

import cv2
import numpy

from bot.recog.image_matcher import image_match, compare_color_equal
from bot.recog.ocr import ocr_line, find_similar_text
from module.umamusume.asset.race_data import RACE_LIST
from module.umamusume.context import UmamusumeContext, SupportCardInfo
from module.umamusume.asset import *
from module.umamusume.define import *
from module.umamusume.script.cultivate_task.const import DATE_YEAR, DATE_MONTH
import bot.base.log as logger

log = logger.get_logger(__name__)


def parse_date(img, ctx: UmamusumeContext) -> int:
    sub_img_date = img[35:75, 10:220]
    sub_img_date = cv2.copyMakeBorder(sub_img_date, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
    date_text = ocr_line(sub_img_date)
    year_text = ""
    for text in DATE_YEAR:
        if date_text.__contains__(text):
            year_text = text

    if year_text == "":
        year_text = find_similar_text(date_text, DATE_YEAR)

    if year_text == DATE_YEAR[3]:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if image_match(img, URA_DATE_1).find_match:
            return 97
        elif image_match(img, URA_DATE_2).find_match:
            return 98
        else:
            return 99

    if year_text == "":
        return -1

    month_text = ""
    for text in DATE_MONTH:
        if date_text.__contains__(text):
            month_text = text
    if month_text == "":
        month_text = find_similar_text(date_text, DATE_MONTH)

    if month_text != DATE_MONTH[0]:
        date_id = DATE_YEAR.index(year_text) * 24 + DATE_MONTH.index(month_text)
    else:
        sub_img_turn_to_race = cv2.copyMakeBorder(img[99:158, 13:140], 20, 20, 20, 20, cv2.BORDER_CONSTANT, None,
                                                  (255, 255, 255))
        turn_to_race_text = ocr_line(sub_img_turn_to_race)
        if turn_to_race_text == "比赛日":
            log.debug("出道比赛日")
            return 12
        turn_to_race_text = re.sub("\\D", "", turn_to_race_text)
        if turn_to_race_text == '':
            log.warning("出道战前日期识别异常")
            return 12 - (len(ctx.cultivate_detail.turn_info_history) + 1)
        date_id = 12 - int(turn_to_race_text)
        if date_id < 1:
            log.warning("出道战前日期识别异常")
            return 12 - (len(ctx.cultivate_detail.turn_info_history) + 1)
    return date_id


def parse_cultivate_main_menu(ctx: UmamusumeContext, img):
    parse_train_main_menu_operations_availability(ctx, img)
    parse_umamusume_remain_stamina_value(ctx, img)
    parse_umamusume_basic_ability_value(ctx, img)
    parse_motivation(ctx, img)
    parse_debut_race(ctx, img)
    ctx.cultivate_detail.turn_info.parse_main_menu_finish = True


def parse_debut_race(ctx: UmamusumeContext, img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if image_match(img, REF_DEBUT_RACE_NOT_WIN).find_match:
        ctx.cultivate_detail.debut_race_win = False
    else:
        ctx.cultivate_detail.debut_race_win = True


def parse_motivation(ctx: UmamusumeContext, img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    for i in range(len(MOTIVATION_LIST)):
        result = image_match(img, MOTIVATION_LIST[i])
        if result.find_match:
            ctx.cultivate_detail.turn_info.motivation_level = MotivationLevel(i + 1)
            return


def parse_umamusume_basic_ability_value(ctx: UmamusumeContext, img):
    sub_img_speed = img[855:885, 70:139]
    sub_img_speed = cv2.copyMakeBorder(sub_img_speed, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
    speed_text = ocr_line(sub_img_speed)

    sub_img_stamina = img[855:885, 183:251]
    sub_img_stamina = cv2.copyMakeBorder(sub_img_stamina, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
    stamina_text = ocr_line(sub_img_stamina)

    sub_img_power = img[855:885, 289:364]
    sub_img_power = cv2.copyMakeBorder(sub_img_power, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
    power_text = ocr_line(sub_img_power)

    sub_img_will = img[855:885, 409:476]
    sub_img_will = cv2.copyMakeBorder(sub_img_will, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
    will_text = ocr_line(sub_img_will)

    sub_img_intelligence = img[855:885, 521:588]
    sub_img_intelligence = cv2.copyMakeBorder(sub_img_intelligence, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None,
                                              (255, 255, 255))
    intelligence_text = ocr_line(sub_img_intelligence)

    sub_img_skill = img[855:902, 602:690]
    sub_img_skill = cv2.copyMakeBorder(sub_img_skill, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None,
                                       (255, 255, 255))
    skill_point_text = ocr_line(sub_img_skill)

    ctx.cultivate_detail.turn_info.uma_attribute.speed = trans_attribute_value(speed_text, ctx,
                                                                               TrainingType.TRAINING_TYPE_SPEED)
    ctx.cultivate_detail.turn_info.uma_attribute.stamina = trans_attribute_value(stamina_text, ctx,
                                                                                 TrainingType.TRAINING_TYPE_STAMINA)
    ctx.cultivate_detail.turn_info.uma_attribute.power = trans_attribute_value(power_text, ctx,
                                                                               TrainingType.TRAINING_TYPE_POWER)
    ctx.cultivate_detail.turn_info.uma_attribute.will = trans_attribute_value(will_text, ctx,
                                                                              TrainingType.TRAINING_TYPE_WILL)
    ctx.cultivate_detail.turn_info.uma_attribute.intelligence = trans_attribute_value(intelligence_text, ctx,
                                                                                      TrainingType.TRAINING_TYPE_INTELLIGENCE)
    ctx.cultivate_detail.turn_info.uma_attribute.skill_point = trans_attribute_value(skill_point_text, ctx)


def trans_attribute_value(text: str, ctx: UmamusumeContext,
                          train_type: TrainingType = TrainingType.TRAINING_TYPE_UNKNOWN) -> int:
    text = re.sub("\\D", "", text)
    if text == "":
        prev_turn_idx = len(ctx.cultivate_detail.turn_info_history)
        if prev_turn_idx != 0:
            history = ctx.cultivate_detail.turn_info_history[prev_turn_idx - 1]
            log.warning("图像识别错误，使用上回合数值")
            if train_type.value == 1:
                return history.uma_attribute.speed
            elif train_type.value == 2:
                return history.uma_attribute.stamina
            elif train_type.value == 3:
                return history.uma_attribute.power
            elif train_type.value == 4:
                return history.uma_attribute.will
            elif train_type.value == 5:
                return history.uma_attribute.intelligence
            else:
                return 0
        else:
            return 100
    else:
        return int(text)


def parse_umamusume_remain_stamina_value(ctx: UmamusumeContext, img):
    sub_img_remain_stamina = img[160:161, 229:505]
    stamina_counter = 0
    for c in sub_img_remain_stamina[0]:
        if not compare_color_equal(c, [117, 117, 117]):
            stamina_counter += 1
    remain_stamina = int(stamina_counter / 276 * 100)
    ctx.cultivate_detail.turn_info.remain_stamina = remain_stamina


def parse_train_main_menu_operations_availability(ctx: UmamusumeContext, img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # 可用性
    btn_rest_check_point = img[980, 60]
    btn_train_check_point = img[990, 250]
    btn_skill_check_point = img[980, 550]
    btn_medic_room_check_point = img[1125, 105]
    btn_trip_check_point = img[1115, 305]
    btn_race_check_point = img[1130, 490]

    # 夏合宿期间
    if 36 < ctx.cultivate_detail.turn_info.date <= 40 or 60 < ctx.cultivate_detail.turn_info.date <= 64:
        btn_medic_room_check_point = img[1130, 200]
        btn_rest_check_point = img[990, 190]
        btn_race_check_point = img[1125, 395]

    rest_available = btn_rest_check_point[0] > 200
    train_available = btn_train_check_point[0] > 200
    skill_available = btn_skill_check_point[0] > 200
    if btn_medic_room_check_point[0] > 200 and btn_medic_room_check_point[1] > 200 and btn_medic_room_check_point[
        2] > 200:
        medic_room_available = True
    else:
        medic_room_available = False
    trip_available = btn_trip_check_point[0] > 200
    race_available = btn_race_check_point[0] > 200

    ctx.cultivate_detail.turn_info.race_available = race_available
    ctx.cultivate_detail.turn_info.medic_room_available = medic_room_available


def parse_training_support_card(ctx: UmamusumeContext, img, train_type: TrainingType):
    base_x = 590
    base_y = 190
    inc = 120
    for i in range(5):
        support_card_icon = img[base_y:base_y + 110, base_x: base_x + 105]
        # 判断好感度
        support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_BGR2RGB)
        favor_process_check_list = [support_card_icon[95, 16], support_card_icon[95, 20]]
        support_card_favor_process = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN
        for support_card_favor_process_pos in favor_process_check_list:
            if compare_color_equal(support_card_favor_process_pos, [255, 235, 120]):
                support_card_favor_process = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4
            elif compare_color_equal(support_card_favor_process_pos, [255, 173, 30]):
                support_card_favor_process = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3
            elif compare_color_equal(support_card_favor_process_pos, [162, 230, 30]):
                support_card_favor_process = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_2
            elif (compare_color_equal(support_card_favor_process_pos, [42, 192, 255]) or
                  compare_color_equal(support_card_favor_process_pos, [109, 108, 117])):
                support_card_favor_process = SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_1
            if support_card_favor_process != SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN:
                break

        # 判断是否有事件
        support_card_event_pos = support_card_icon[5, 83]
        support_card_event_available = False
        if (support_card_event_pos[0] >= 250
                and 55 <= support_card_event_pos[1] <= 90
                and 115 <= support_card_event_pos[2] <= 150):
            support_card_event_available = True
        # 判断支援卡类型
        support_card_type = SupportCardType.SUPPORT_CARD_TYPE_UNKNOWN
        support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_RGB2GRAY)
        if image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_SPEED).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_SPEED
        elif image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_STAMINA).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_STAMINA
        elif image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_POWER).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_POWER
        elif image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_WILL).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_WILL
        elif image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_INTELLIGENCE).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_INTELLIGENCE
        elif image_match(support_card_icon, REF_SUPPORT_CARD_TYPE_FRIEND).find_match:
            support_card_type = SupportCardType.SUPPORT_CARD_TYPE_FRIEND
        if support_card_favor_process is not SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN:
            info = SupportCardInfo(card_type=support_card_type,
                                   favor=support_card_favor_process,
                                   has_event=support_card_event_available)
            ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].support_card_info_list.append(info)
        base_y += inc


def parse_train_type(ctx: UmamusumeContext, img) -> TrainingType:
    train_label = cv2.cvtColor(img[210:275, 0:210], cv2.COLOR_RGB2GRAY)
    train_type = TrainingType.TRAINING_TYPE_UNKNOWN
    if image_match(train_label, REF_TRAINING_TYPE_SPEED).find_match:
        train_type = TrainingType.TRAINING_TYPE_SPEED
    elif image_match(train_label, REF_TRAINING_TYPE_STAMINA).find_match:
        train_type = TrainingType.TRAINING_TYPE_STAMINA
    elif image_match(train_label, REF_TRAINING_TYPE_POWER).find_match:
        train_type = TrainingType.TRAINING_TYPE_POWER
    elif image_match(train_label, REF_TRAINING_TYPE_WILL).find_match:
        train_type = TrainingType.TRAINING_TYPE_WILL
    elif image_match(train_label, REF_TRAINING_TYPE_INTELLIGENCE).find_match:
        train_type = TrainingType.TRAINING_TYPE_INTELLIGENCE
    return train_type


def parse_training_result(ctx: UmamusumeContext, img, train_type: TrainingType):
    sub_img_speed_incr = img[770:826, 30:140]
    speed_incr_text = ocr_line(sub_img_speed_incr)
    speed_incr_text = re.sub("\\D", "", speed_incr_text)

    sub_img_stamina_incr = img[770:826, 140:250]
    stamina_incr_text = ocr_line(sub_img_stamina_incr)
    stamina_incr_text = re.sub("\\D", "", stamina_incr_text)

    sub_img_power_incr = img[770:826, 250:360]
    power_incr_text = ocr_line(sub_img_power_incr)
    power_incr_text = re.sub("\\D", "", power_incr_text)

    sub_img_will_incr = img[770:826, 360:470]
    will_incr_text = ocr_line(sub_img_will_incr)
    will_incr_text = re.sub("\\D", "", will_incr_text)

    sub_img_intelligence_incr = img[770:826, 470:580]
    intelligence_incr_text = ocr_line(sub_img_intelligence_incr)
    intelligence_incr_text = re.sub("\\D", "", intelligence_incr_text)

    sub_img_skill_point_incr = img[770:826, 588:695]
    skill_point_incr_text = ocr_line(sub_img_skill_point_incr)
    skill_point_incr_text = re.sub("\\D", "", skill_point_incr_text)

    if speed_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].speed_incr = int(
            speed_incr_text)
    if stamina_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].stamina_incr = int(
            stamina_incr_text)
    if power_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].power_incr = int(
            power_incr_text)
    if will_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].will_incr = int(
            will_incr_text)
    if intelligence_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].intelligence_incr = int(
            intelligence_incr_text)
    if skill_point_incr_text != "":
        ctx.cultivate_detail.turn_info.training_info_list[train_type.value - 1].skill_point_incr = int(
            skill_point_incr_text)


def find_support_card(ctx: UmamusumeContext, img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    while True:
        match_result = image_match(img, REF_FOLLOW_SUPPORT_CARD_DETECT_LABEL)
        if match_result.find_match:
            pos = match_result.matched_area
            support_card_info = img[pos[0][1] - 125:pos[1][1] + 10, pos[0][0] - 140: pos[1][0] + 380]
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0
            support_card_level_img = support_card_info[125:145, 68:111]
            support_card_name_img = support_card_info[63:94, 132:439]

            support_card_level_img = cv2.copyMakeBorder(support_card_level_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT,
                                                        None,
                                                        (255, 255, 255))
            support_card_name_img = cv2.copyMakeBorder(support_card_name_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None,
                                                       (255, 255, 255))
            support_card_level_text = ocr_line(support_card_level_img)
            if support_card_level_text == "":
                continue
            support_card_level = int(re.sub("\\D", "", support_card_level_text))
            if support_card_level < ctx.cultivate_detail.follow_support_card_level:
                continue
            support_card_text = ocr_line(support_card_name_img)
            s = SequenceMatcher(None, support_card_text, ctx.cultivate_detail.follow_support_card_name)
            if s.ratio() > 0.7:
                ctx.ctrl.click(match_result.center_point[0], match_result.center_point[1] - 75,
                               "选择支援卡：" + ctx.cultivate_detail.follow_support_card_name + "<" + str(
                                   support_card_level) + ">")
                return True
        else:
            break
    return False


# 111 237 480 283
def parse_cultivate_event(ctx: UmamusumeContext, img) -> (str, list[int]):
    event_name_img = img[237:283, 111:480]
    event_name = ocr_line(event_name_img)
    event_selector_list = []
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    while True:
        match_result = image_match(img, REF_SELECTOR)
        if match_result.find_match:
            event_selector_list.append(match_result.center_point)
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0
        else:
            break
    event_selector_list.sort(key=lambda x: x[1])
    return event_name, event_selector_list


def find_race(ctx: UmamusumeContext, img, race_id: int = 0) -> bool:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    target_race_template = RACE_LIST[race_id][2]
    while True:
        match_result = image_match(img, REF_RACE_LIST_DETECT_LABEL)
        if match_result.find_match:
            pos = match_result.matched_area
            pos_center = match_result.center_point
            if 685 < pos_center[1] < 1110:
                race_name_img = img[pos[0][1] - 60:pos[1][1] + 25, pos[0][0] - 250: pos[1][0] + 400]
                if target_race_template is not None:
                    if image_match(race_name_img, target_race_template).find_match:
                        ctx.ctrl.click(match_result.center_point[0], match_result.center_point[1],
                                       "选择比赛：" + str(RACE_LIST[race_id][1]))
                        return True
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0
        else:
            break
    return False


# 490 400 665 440 525 69 588 99
def find_skill(ctx: UmamusumeContext, img, skill: list[str], learn_any_skill: bool) -> bool:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    find = False
    while True:
        match_result = image_match(img, REF_SKILL_LIST_DETECT_LABEL)
        if match_result.find_match:
            pos = match_result.matched_area
            pos_center = match_result.center_point
            if 460 < pos_center[0] < 560 and 450 < pos_center[1] < 1050:
                skill_info_img = img[pos[0][1] - 65:pos[1][1] + 75, pos[0][0] - 470: pos[1][0] + 150]
                if not image_match(skill_info_img, REF_SKILL_LEARNED).find_match:
                    skill_name_img = skill_info_img[10: 47, 100: 445]
                    skill_cost_img = skill_info_img[65: 95, 520: 580]
                    text = ocr_line(skill_name_img)
                    cost = ocr_line(skill_cost_img)
                    result = find_similar_text(text, skill, 0.7)
                    # print(text + "->" + result)
                    if result != "" or learn_any_skill:
                        tmp_img = ctx.ctrl.get_screen()
                        pt_text = re.sub("\\D", "", ocr_line(tmp_img[400: 440, 490: 665]))
                        skill_pt_cost_text = re.sub("\\D", "", ocr_line(skill_info_img[69: 99, 525: 588]))
                        if pt_text != "" and skill_pt_cost_text != "":
                            pt = int(pt_text)
                            skill_pt_cost = int(skill_pt_cost_text)
                            if pt >= skill_pt_cost:
                                ctx.ctrl.click(match_result.center_point[0] + 128, match_result.center_point[1],
                                               "加点技能：" + text)
                                ctx.cultivate_detail.learn_skill_selected = True
                                find = True

            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0

        else:
            break
    return find


def get_skill_list(img, skill: list[str]) -> list:
    imgcp = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = []
    while True:
        match_result = image_match(img, REF_SKILL_LIST_DETECT_LABEL)
        if match_result.find_match:
            pos = match_result.matched_area
            pos_center = match_result.center_point
            if 460 < pos_center[0] < 560 and 450 < pos_center[1] < 1050:
                skill_info_img = img[pos[0][1] - 65:pos[1][1] + 75, pos[0][0] - 470: pos[1][0] + 150]
                skill_info_cp = imgcp[pos[0][1] - 65:pos[1][1] + 75, pos[0][0] - 470: pos[1][0] + 150]
                if not image_match(skill_info_img, REF_SKILL_LEARNED).find_match:
                    skill_name_img = skill_info_img[10: 47, 100: 445]
                    skill_cost_img = skill_info_img[69: 99, 525: 588]
                    text = ocr_line(skill_name_img)
                    cost = re.sub("\\D", "", ocr_line(skill_cost_img))
                    
                    #检查是不是金色技能
                    mask = cv2.inRange(skill_info_cp,numpy.array([40,180,240]),numpy.array([100,210,255]))
                    isGold = True if mask[120,600] == 255 else False

                    flag = False
                    for i in range(len(skill)):
                        if text in skill[i]:
                            priority = i
                            flag = True
                    if flag == False:
                        priority = len(skill)
                    res.append({"skill_name":text,
                                "skill_cost":int(cost),
                                "priority":priority,
                                "is_gold":isGold,
                                "subsequent_skill":"",
                                "is_available":True,
                                "y_pos":int(pos_center[1])})
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0

        else:
            break
    res = sorted(res,key = lambda x : x["y_pos"])
    #没有精确计算过，但是大约y轴小于540就会导致技能名显示不全。暂时没测试出问题。
    return [{k: v for k,v in r.items() if k != "y_pos"} for r in res if r["y_pos"] >= 540]

def parse_factor(ctx: UmamusumeContext):
    origin_img = ctx.ctrl.get_screen()
    img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
    factor_list = []
    while True:
        match_result = image_match(img, REF_FACTOR_DETECT_LABEL)
        if match_result.find_match:
            factor_info = ['unknown', 0]
            pos = match_result.matched_area
            factor_info_img_gray = img[pos[0][1] - 20:pos[1][1] + 25, pos[0][0] - 630: pos[1][0] - 25]
            factor_info_img = origin_img[pos[0][1] - 20:pos[1][1] + 25, pos[0][0] - 630: pos[1][0] - 25]
            factor_name_sub_img = factor_info_img_gray[15: 60, 45:320]
            factor_name = ocr_line(factor_name_sub_img)
            factor_level = 0
            factor_level_check_point = [factor_info_img[35, 535], factor_info_img[35, 565], factor_info_img[35, 595]]
            for i in range(len(factor_level_check_point)):
                if not compare_color_equal(factor_level_check_point[i], [223, 227, 237]):
                    factor_level += 1
                else:
                    break
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
                match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0
            factor_info[0] = factor_name
            factor_info[1] = factor_level
            factor_list.append(factor_info)
        else:
            break
    ctx.cultivate_detail.parse_factor_done = True
    ctx.task.detail.cultivate_result['factor_list'] = factor_list
