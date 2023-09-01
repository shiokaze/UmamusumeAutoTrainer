import cv2
import numpy as np

from bot.base.common import ImageMatchMode
from bot.base.resource import Template
import bot.base.log as logger

log = logger.get_logger(__name__)


class ImageMatchResult:
    # matched_area 匹配结果区域 [100, 100]
    matched_area = None
    # center_point 匹配结果的中心点
    center_point = None
    # find_match 匹配是否成功
    find_match: bool = False
    # score 匹配的相似得分（仅用于特征匹配）
    score: int = 0


def image_match(target, template: Template) -> ImageMatchResult:

    try:
        if template.image_match_config.match_mode == ImageMatchMode.IMAGE_MATCH_MODE_TEMPLATE_MATCH:
            return template_match(target, template.template_image, template.image_match_config.match_accuracy)
        else:
            log.error("unsupported match mode")
    except Exception as e:
        log.error(f"image_match failed: {e}")
        return ImageMatchResult()


def template_match(target, template, accuracy: float = 0.95) -> ImageMatchResult:
    th, tw = template.shape[::]
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    match_result = ImageMatchResult()
    if max_val > accuracy:
        match_result.find_match = True
        match_result.center_point = (int(max_loc[0] + tw / 2), int(max_loc[1] + th / 2))
        match_result.matched_area = ((max_loc[0], max_loc[1]), (max_loc[0] + tw, max_loc[1] + th))
    else:
        match_result.find_match = False
    return match_result


def compare_color_equal(p: list, target: list, tolerance: int = 10) -> bool:
    distance = np.sqrt(np.sum((np.array(target) - np.array(p)) ** 2))
    return distance < tolerance
