import time

import cv2

from bot.base.task import TaskStatus, EndTaskReason
from bot.recog.image_matcher import image_match
from bot.recog.ocr import ocr_line, find_similar_text
from module.umamusume.asset.point import *
from module.umamusume.asset.ui import INFO
from module.umamusume.context import UmamusumeContext
import bot.base.log as logger

log = logger.get_logger(__name__)

TITLE = [
    "赛事详情",
    "休息&外出确认",
    "网络错误",
    "重新挑战",
    "获得誉名",
    "完成养成",
    "缩短事件设置",
    "外出确认",
    "技能获取确认",
    "成功获得技能",
    "养成结束确认",
    "优俊少女详情",
    "粉丝数未达到目标赛事要求",
    "外出",
    "跳过确认",
    "休息确认",
    "赛事推荐功能",
    "战术",
    "目标粉丝数不足",
    "连续参赛",
    "医务室确认",
    "礼物箱",
    "领取成功",
    "解锁角色剧情",
    "目标达成次数不足"
]


def script_info(ctx: UmamusumeContext):
    img = ctx.current_screen
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = image_match(img, UI_INFO)
    if result.find_match:
        pos = result.matched_area
        title_img = img[pos[0][1] - 5:pos[1][1] + 5, pos[0][0] + 150: pos[1][0] + 405]
        title_text = ocr_line(title_img)
        print(title_text)
        title_text = find_similar_text(title_text, TITLE, 0.8)
        if title_text == "":
            log.warning("未知的选项框")
            return
        if title_text == TITLE[0]:
            ctx.ctrl.click_by_point(CULTIVATE_GOAL_RACE_INTER_3)
        if title_text == TITLE[1]:
            ctx.ctrl.click_by_point(INFO_SUMMER_REST_CONFIRM)
        if title_text == TITLE[2]:
            ctx.ctrl.click_by_point(NETWORK_ERROR_CONFIRM)
        if title_text == TITLE[3]:
            if ctx.prev_ui is INFO:
                ctx.cultivate_detail.clock_used -= 1
            if ctx.cultivate_detail.clock_use_limit > ctx.cultivate_detail.clock_used:
                ctx.ctrl.click_by_point(RACE_FAIL_CONTINUE_USE_CLOCK)
                ctx.cultivate_detail.clock_used += 1
            else:
                ctx.ctrl.click_by_point(RACE_FAIL_CONTINUE_CANCEL)
            log.debug("闹钟限制%s,已使用%s", str(ctx.cultivate_detail.clock_use_limit),
                      str(ctx.cultivate_detail.clock_used))
        if title_text == TITLE[4]:
            ctx.ctrl.click_by_point(GET_TITLE_CONFIRM)
        if title_text == TITLE[5]:
            ctx.ctrl.click_by_point(CULTIVATE_FINISH_RETURN_CONFIRM)
        if title_text == TITLE[6]:
            ctx.ctrl.click_by_point(SCENARIO_SHORTEN_SET_2)
            time.sleep(0.5)
            ctx.ctrl.click_by_point(SCENARIO_SHORTEN_CONFIRM)
        if title_text == TITLE[7]:
            ctx.ctrl.click_by_point(CULTIVATE_OPERATION_COMMON_CONFIRM)
        if title_text == TITLE[8]:
            ctx.ctrl.click_by_point(CULTIVATE_LEARN_SKILL_CONFIRM_AGAIN)
        if title_text == TITLE[9]:
            ctx.ctrl.click_by_point(CULTIVATE_LEARN_SKILL_DONE_CONFIRM)
            ctx.cultivate_detail.learn_skill_selected = False
        if title_text == TITLE[10]:
            ctx.ctrl.click_by_point(CULTIVATE_FINISH_CONFIRM_AGAIN)
        if title_text == TITLE[11]:
            ctx.ctrl.click_by_point(CULTIVATE_RESULT_CONFIRM)
        if title_text == TITLE[12]:
            ctx.ctrl.click_by_point(CULTIVATE_FAN_NOT_ENOUGH_RETURN)
        if title_text == TITLE[13]:
            ctx.ctrl.click_by_point(CULTIVATE_TRIP_WITH_FRIEND)
        if title_text == TITLE[14]:
            ctx.ctrl.click_by_point(SKIP_CONFIRM)
        if title_text == TITLE[15]:
            ctx.ctrl.click_by_point(CULTIVATE_OPERATION_COMMON_CONFIRM)
        if title_text == TITLE[16]:
            ctx.ctrl.click_by_point(RACE_RECOMMEND_CONFIRM)
        if title_text == TITLE[17]:
            date = ctx.cultivate_detail.turn_info.date
            if date != -1:
                if date <= 72:
                    ctx.ctrl.click_by_point(TACTIC_LIST[ctx.cultivate_detail.tactic_list[int((date - 1)/ 24)] - 1])
                else:
                    ctx.ctrl.click_by_point(TACTIC_LIST[ctx.cultivate_detail.tactic_list[2] - 1])
            time.sleep(0.5)
            ctx.ctrl.click_by_point(BEFORE_RACE_CHANGE_TACTIC_CONFIRM)
        if title_text == TITLE[18]:
            ctx.ctrl.click_by_point(CULTIVATE_FAN_NOT_ENOUGH_RETURN)
        if title_text == TITLE[19]:
            ctx.ctrl.click_by_point(CULTIVATE_TOO_MUCH_RACE_WARNING_CONFIRM)
        if title_text == TITLE[20]:
            ctx.ctrl.click_by_point(CULTIVATE_OPERATION_COMMON_CONFIRM)
        if title_text == TITLE[21]:
            ctx.ctrl.click_by_point(RECEIVE_GIFT)
        if title_text == TITLE[22]:
            ctx.ctrl.click_by_point(RECEIVE_GIFT_SUCCESS_CLOSE)
        if title_text == TITLE[23]:
            ctx.ctrl.click_by_point(UNLOCK_STORY_TO_HOME_PAGE)
        if title_text == TITLE[24]:
            ctx.ctrl.click_by_point(WIN_TIMES_NOT_ENOUGH_RETURN)
        time.sleep(1)

