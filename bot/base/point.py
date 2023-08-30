from enum import Enum

from bot.base.common import Coordinate
from bot.base.resource import Template


class ClickPointType(Enum):
    CLICK_POINT_TYPE_COORDINATE = 0
    CLICK_POINT_TYPE_TEMPLATE = 1


class ClickPoint:
    target_type: ClickPointType = None
    template: Template | None = None
    coordinate: Coordinate = None
    desc: str = None
    template_check_list: list[Template] = None

    def __init__(self, target_type: ClickPointType, template: Template = None, coordinate: Coordinate = None,
                 desc: str = "", template_check_list: list[Template] = None):
        self.target_type = target_type
        self.desc = desc
        self.template_check_list = template_check_list
        self.coordinate = coordinate
        self.template = template







