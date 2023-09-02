import cv2

from bot.recog.image_matcher import image_match
from module.umamusume.context import UmamusumeContext
from module.umamusume.script.cultivate_task.ai import get_operation
from module.umamusume.asset.point import *
import bot.base.log as logger

log = logger.get_logger(__name__)


def before_hook(ctx: UmamusumeContext):
    pass


def after_hook(ctx: UmamusumeContext):
    img = cv2.cvtColor(ctx.current_screen, cv2.COLOR_BGR2GRAY)
    if image_match(img, BTN_SKIP).find_match:
        ctx.ctrl.click_by_point(SKIP)
    if image_match(img, BTN_SKIP_OFF).find_match:
        ctx.ctrl.click_by_point(SCENARIO_SKIP_OFF)
    if image_match(img, BTN_SKIP_SPEED_1).find_match:
        ctx.ctrl.click_by_point(SCENARIO_SKIP_SPEED_1)
    if ctx.cultivate_detail and ctx.cultivate_detail.turn_info is not None:
        if ctx.cultivate_detail.turn_info.parse_train_info_finish and ctx.cultivate_detail.turn_info.parse_main_menu_finish:
            if not ctx.cultivate_detail.turn_info.turn_info_logged:
                ctx.cultivate_detail.turn_info.log_turn_info()
                ctx.cultivate_detail.turn_info.turn_info_logged = True
            if ctx.cultivate_detail.turn_info.turn_operation is None:
                ctx.cultivate_detail.turn_info.turn_operation = get_operation(ctx)
                ctx.cultivate_detail.turn_info.turn_operation.log_turn_operation()




