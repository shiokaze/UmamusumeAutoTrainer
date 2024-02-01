import time

import cv2

from bot.base.task import TaskStatus, EndTaskReason
from module.umamusume.task import EndTaskReason as UEndTaskReason
from bot.recog.image_matcher import image_match
from bot.recog.ocr import ocr_line, find_similar_text
from module.umamusume.asset.point import *
from module.umamusume.asset.ui import INFO
from module.umamusume.context import UmamusumeContext
from .race import script_team_stadium_no_rp, script_team_stadium_select_item, script_team_stadium_time_sale
from .time_sale import script_time_sale_close_confirm, script_time_sale_buy_confirm, script_time_sale_buy_success
import bot.base.log as logger

log = logger.get_logger(__name__)

TITLE = {
    "网络错误": lambda ctx: ctx.ctrl.click_by_point(NETWORK_ERROR_CONFIRM),
    "解锁角色剧情": lambda ctx: ctx.ctrl.click_by_point(UNLOCK_STORY_TO_HOME_PAGE),
    "活动剧情解锁": lambda ctx: ctx.ctrl.click_by_point(ACTIVITY_STORY_UNLOCK_CONFIRM) or
                                ctx.ctrl.click_by_point(ACTIVITY_STORY_UNLOCK_CONFIRM2),
    "公告": lambda ctx: ctx.ctrl.click_by_point(CLOSE_NEWS),
    "礼物箱": lambda ctx: ctx.ctrl.click_by_point(RECEIVE_GIFT),
    "领取成功": lambda ctx: ctx.ctrl.click_by_point(RECEIVE_GIFT_SUCCESS_CLOSE),
    "日期变化": lambda ctx: ctx.ctrl.click_by_point(DATE_CHANGE_CONFIRM),
    "连接已断开": lambda ctx: ctx.ctrl.click_by_point(CONNECTION_LOST_RESUME),
    "选择道具": script_team_stadium_select_item,
    "限时特卖开售": script_team_stadium_time_sale,
    "确认": script_team_stadium_no_rp,
    "兑换确认": script_time_sale_buy_confirm,
    "兑换成功": script_time_sale_buy_success,
    "重置确认": script_time_sale_close_confirm,
}


def ts_script_info(ctx: UmamusumeContext):
    img = ctx.current_screen
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = image_match(img, UI_INFO)
    if result.find_match:
        pos = result.matched_area
        title_img = img[pos[0][1] - 5:pos[1][1] + 5, pos[0][0] + 150: pos[1][0] + 405]
        title_text = ocr_line(title_img)
        log.debug(title_text)
        title_text = find_similar_text(title_text, TITLE, 0.8)
        if title_text == "":
            log.warning("未知的选项框")
            return
        TITLE[title_text](ctx)
