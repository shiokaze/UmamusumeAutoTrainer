from module.umamusume.context import UmamusumeContext
from module.umamusume.define import TurnOperationType
from module.umamusume.asset.template import REF_SELECTOR, REF_AOHARUHAI_TEAM_NAME
from bot.recog.image_matcher import image_match

import bot.base.log as logger
log = logger.get_logger(__name__)

# 第一年新年事件
def scenario_event_1(ctx: UmamusumeContext) -> int:
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and ctx.cultivate_detail.turn_info.remain_stamina >= 50 or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and ctx.cultivate_detail.turn_info.remain_stamina >= 50:
        return 3
    else:
        return 2


# 第二年新年事件
def scenario_event_2(ctx: UmamusumeContext) -> int:
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and ctx.cultivate_detail.turn_info.remain_stamina >= 40 or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and ctx.cultivate_detail.turn_info.remain_stamina >= 50:
        return 3
    else:
        return 1
    
# 青春杯队伍名称选择事件
def aoharuhai_team_name_event(ctx: UmamusumeContext) -> int:
    img = ctx.ctrl.get_screen(to_gray=True)
    event_selector_list = []
    while True:
        match_result = image_match(img, REF_SELECTOR)
        if match_result.find_match:
            event_selector_list.append(match_result)
            img[match_result.matched_area[0][1]:match_result.matched_area[1][1],
            match_result.matched_area[0][0]:match_result.matched_area[1][0]] = 0
        else:
            break
    event_selector_list.sort(key=lambda x: x.center_point[1])
    for i in range(len(event_selector_list)):
        event = event_selector_list[i]
        event_img = img[event.matched_area[0][1]-20:event.matched_area[1][1]+20, 0:720]
        if image_match(event_img, REF_AOHARUHAI_TEAM_NAME[ctx.task.detail.scenario_config.aoharu_config.aoharu_team_name_selection]).find_match:
            log.debug("匹配到设置的青春杯队伍名")
            return i + 1

    log.debug("未匹配到设置的青春杯队伍名, 使用默认选项<胡萝卜>队")
    return len(event_selector_list)
