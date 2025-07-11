import re
import cv2
import time

from .base_scenario import BaseScenario
from module.umamusume.asset import *
from module.umamusume.define import ScenarioType, SupportCardFavorLevel, SupportCardType
from module.umamusume.types import SupportCardInfo
from bot.recog.image_matcher import image_match, compare_color_equal
from bot.recog.ocr import ocr_line, find_similar_text, ocr_digits

import bot.base.log as logger
log = logger.get_logger(__name__)

class AoharuHaiScenario(BaseScenario):
    def __init__(self):
        super().__init__()

    def scenario_type(self) -> ScenarioType:
        return ScenarioType.SCENARIO_TYPE_AOHARUHAI
    
    def scenario_name(self) -> str:
        return "青春杯"
    
    def get_date_img(self, img: any) -> any:
        return img[40:70, 160:370]
    
    def get_turn_to_race_img(self, img) -> any:
        return img[70:120, 30:90]
    
    def parse_training_result(self, img: any) -> list[int]:
        # 使用数字ocr达到更高准确率
        sub_img_speed_incr = img[800:830, 30:140]
        sub_img_speed_incr = cv2.copyMakeBorder(sub_img_speed_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        speed_incr_text = ocr_digits(sub_img_speed_incr)
        speed_incr_text = re.sub("\\D", "", speed_incr_text)

        sub_img_speed_incr_extra = img[760:800, 30:140]
        sub_img_speed_incr_extra = cv2.copyMakeBorder(sub_img_speed_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        speed_incr_extra_text = ocr_digits(sub_img_speed_incr_extra)
        speed_incr_extra_text = re.sub("\\D", "", speed_incr_extra_text)

        sub_img_stamina_incr = img[800:830, 140:250]
        sub_img_stamina_incr = cv2.copyMakeBorder(sub_img_stamina_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        stamina_incr_text = ocr_digits(sub_img_stamina_incr)
        stamina_incr_text = re.sub("\\D", "", stamina_incr_text)

        sub_img_stamina_incr_extra = img[760:800, 140:250]
        sub_img_stamina_incr_extra = cv2.copyMakeBorder(sub_img_stamina_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        stamina_incr_extra_text = ocr_digits(sub_img_stamina_incr_extra)
        stamina_incr_extra_text = re.sub("\\D", "", stamina_incr_extra_text)

        sub_img_power_incr = img[800:830, 250:360]
        sub_img_power_incr = cv2.copyMakeBorder(sub_img_power_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        power_incr_text = ocr_digits(sub_img_power_incr)
        power_incr_text = re.sub("\\D", "", power_incr_text)

        sub_img_power_incr_extra = img[760:800, 250:360]
        sub_img_power_incr_extra = cv2.copyMakeBorder(sub_img_power_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        power_incr_extra_text = ocr_digits(sub_img_power_incr_extra)
        power_incr_extra_text = re.sub("\\D", "", power_incr_extra_text)

        sub_img_will_incr = img[800:830, 360:470]
        sub_img_will_incr = cv2.copyMakeBorder(sub_img_will_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        will_incr_text = ocr_digits(sub_img_will_incr)
        will_incr_text = re.sub("\\D", "", will_incr_text)

        sub_img_will_incr_extra = img[760:800, 360:470]
        sub_img_will_incr_extra = cv2.copyMakeBorder(sub_img_will_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        will_incr_extra_text = ocr_digits(sub_img_will_incr_extra)
        will_incr_extra_text = re.sub("\\D", "", will_incr_extra_text)

        sub_img_intelligence_incr = img[800:830, 470:580]
        sub_img_intelligence_incr = cv2.copyMakeBorder(sub_img_intelligence_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        intelligence_incr_text = ocr_digits(sub_img_intelligence_incr)
        intelligence_incr_text = re.sub("\\D", "", intelligence_incr_text)

        sub_img_intelligence_incr_extra = img[760:800, 470:580]
        sub_img_intelligence_incr_extra = cv2.copyMakeBorder(sub_img_intelligence_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        intelligence_incr_extra_text = ocr_digits(sub_img_intelligence_incr_extra)
        intelligence_incr_extra_text = re.sub("\\D", "", intelligence_incr_extra_text)

        sub_img_skill_point_incr = img[800:830, 588:695]
        sub_img_skill_point_incr = cv2.copyMakeBorder(sub_img_skill_point_incr, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        skill_point_incr_text = ocr_digits(sub_img_skill_point_incr)
        skill_point_incr_text = re.sub("\\D", "", skill_point_incr_text)

        sub_img_skill_point_incr_extra = img[760:800, 588:695]
        sub_img_skill_point_incr_extra = cv2.copyMakeBorder(sub_img_skill_point_incr_extra, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, (255, 255, 255))
        skill_point_incr_extra_text = ocr_digits(sub_img_skill_point_incr_extra)
        skill_point_incr_extra_text = re.sub("\\D", "", skill_point_incr_extra_text)

        speed_icr = (0 if speed_incr_text == "" else int(speed_incr_text)) + (0 if speed_incr_extra_text == "" else int(speed_incr_extra_text))
        stamina_incr = (0 if stamina_incr_text == "" else int(stamina_incr_text)) + (0 if stamina_incr_extra_text == "" else int(stamina_incr_extra_text))
        power_incr = (0 if power_incr_text == "" else int(power_incr_text)) + (0 if power_incr_extra_text == "" else int(power_incr_extra_text))
        will_incr = (0 if will_incr_text == "" else int(will_incr_text)) + (0 if will_incr_extra_text == "" else int(will_incr_extra_text))
        intelligence_incr = (0 if intelligence_incr_text == "" else int(intelligence_incr_text)) + (0 if intelligence_incr_extra_text == "" else int(intelligence_incr_extra_text))
        skill_point_incr = (0 if skill_point_incr_text == "" else int(skill_point_incr_text)) + (0 if skill_point_incr_extra_text == "" else int(skill_point_incr_extra_text))

        return [speed_icr, stamina_incr, power_incr, will_incr, intelligence_incr, skill_point_incr]

    def parse_training_support_card(self, img: any) -> list[SupportCardInfo]:
        base_x = 550
        base_y = 177
        inc = 115
        support_card_list_info_result: list[SupportCardInfo] = []
        for i in range(5):
            support_card_icon = img[base_y:base_y + inc, base_x: base_x + 145]
            
            # 有青春杯训练, 且青春杯友情未满
            can_incr_aoharu_train = detect_aoharu_train_arrow(support_card_icon) and aoharu_train_not_full(support_card_icon)
            
            # 判断好感度
            support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_BGR2RGB)
            favor_process_check_list = [support_card_icon[106, 56], support_card_icon[106, 60]]
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
            if (can_incr_aoharu_train) or \
               (support_card_favor_process is not SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN):
                info = SupportCardInfo(card_type=support_card_type,
                                       favor=support_card_favor_process,
                                       can_incr_aoharu_train=can_incr_aoharu_train)
                support_card_list_info_result.append(info)
            base_y += inc

        return support_card_list_info_result
    
# 检测支援卡右上角是否有箭头图标, 同时排除感叹号防止false positive
# 输入的图片必须是彩色的
def detect_aoharu_train_arrow(support_card_icon):
    support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_BGR2RGB)
    # 定义右上角检测区域
    arrow_region_x_start = 110
    arrow_region_x_end = 145  
    arrow_region_y_start = 0
    arrow_region_y_end = 40
    
    arrow_region = support_card_icon[arrow_region_y_start:arrow_region_y_end, 
                                     arrow_region_x_start:arrow_region_x_end]
    
    # 定义箭头可能的颜色范围 (检查橙色)
    orange_lower = [240, 100, 50]
    orange_upper = [255, 180, 100]
    
    # 定义红色像素范围（用于检测感叹号）
    red_lower = [180, 30,50]
    red_upper = [255, 100, 150]
    
    # 计算橙色像素和红色像素的数量
    orange_pixels = 0
    red_pixels = 0
    total_pixels = arrow_region.shape[0] * arrow_region.shape[1]
    
    for y in range(arrow_region.shape[0]):
        for x in range(arrow_region.shape[1]):
            pixel = arrow_region[y, x]
            
            # 检测橙色像素
            if (orange_lower[0] <= pixel[0] <= orange_upper[0] and
                orange_lower[1] <= pixel[1] <= orange_upper[1] and
                orange_lower[2] <= pixel[2] <= orange_upper[2]):
                orange_pixels += 1
            # 检测红色像素
            elif (red_lower[0] <= pixel[0] <= red_upper[0] and
                  red_lower[1] <= pixel[1] <= red_upper[1] and
                  red_lower[2] <= pixel[2] <= red_upper[2]):
                red_pixels += 1
    
    orange_ratio = orange_pixels / total_pixels if total_pixels > 0 else 0
    red_ratio = red_pixels / total_pixels if total_pixels > 0 else 0
    
    has_arrow = False
    
    # 首先排除感叹号：如果红色像素比例过高，判断为感叹号
    if red_ratio > 0.2:
        has_arrow = False
    # 如果橙色像素比例超过阈值
    elif (orange_ratio > 0.05):
        has_arrow = True
 
    return has_arrow


# 检测左下角青春杯训练值是否未满
# 如果已满或者不存在UI(比如已经触发了魂爆, 则返回false)
# 否则返回true
def aoharu_train_not_full(support_card_icon) -> bool:
    support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_BGR2RGB)
    avatar_region_x_start = 5
    avatar_region_x_end = 45
    avatar_region_y_start = 70  
    avatar_region_y_end = 110
    
    avatar_region = support_card_icon[avatar_region_y_start:avatar_region_y_end,
                                      avatar_region_x_start:avatar_region_x_end]
    
    total_pixels = avatar_region.shape[0] * avatar_region.shape[1]
    if total_pixels == 0:
        return False
    
    # 检测灰色
    grey_lower = [100, 100, 100]
    grey_upper = [150, 150, 150]
    grey_pixels = 0

    for y in range(avatar_region.shape[0]):
        for x in range(avatar_region.shape[1]):
            pixel = avatar_region[y, x]
            if (grey_lower[0] <= pixel[0] <= grey_upper[0] and
                grey_lower[1] <= pixel[1] <= grey_upper[1] and
                grey_lower[2] <= pixel[2] <= grey_upper[2]):
                grey_pixels += 1
    
    grey_ratio = grey_pixels / total_pixels
    
    if grey_ratio > 0.05:
        status = True
    else:
        status = False
    
    return status