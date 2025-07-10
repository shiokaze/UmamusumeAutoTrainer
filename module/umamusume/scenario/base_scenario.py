from abc import ABC, abstractmethod
from module.umamusume.define import ScenarioType
from module.umamusume.types import SupportCardInfo

class BaseScenario(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def scenario_type(self) -> ScenarioType:
        """获取剧本类型"""
        pass

    @abstractmethod
    def scenario_name(self) -> str:
        """获取剧本名称"""
        pass

    @abstractmethod
    def get_date_img(self, img: any) -> any:
        """获取屏幕截图上显示日期的部分"""
        pass

    @abstractmethod
    def get_turn_to_race_img(self, img: any) -> any:
        """获取屏幕上距离比赛日期的部分"""
        pass

    @abstractmethod
    def parse_training_result(self, img: any) -> list[int]:
        """从屏幕上获取每一种训练增加的属性值"""
        pass

    @abstractmethod
    def parse_training_support_card(self, img: any) -> list[SupportCardInfo]:
        """从屏幕上获取每一张支援卡的信息"""
        pass
