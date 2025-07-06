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
        return img[40:70, 160:280]
    
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
    
    def parse_training_support_cord(self, img: any) -> list[SupportCardInfo]:
        # TODO: 目前没有识别青春杯参数和青春杯友情条, 也没有将其作为训练权重的一部分,
        base_x = 590
        base_y = 177
        inc = 115
        support_card_list_info_result: list[SupportCardInfo] = []
        for i in range(5):
            support_card_icon = img[base_y:base_y + inc, base_x: base_x + 105]
            # 判断好感度
            support_card_icon = cv2.cvtColor(support_card_icon, cv2.COLOR_BGR2RGB)
            favor_process_check_list = [support_card_icon[106, 16], support_card_icon[106, 20]]
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
                support_card_list_info_result.append(info)
            base_y += inc

        return support_card_list_info_result