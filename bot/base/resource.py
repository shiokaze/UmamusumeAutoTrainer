import cv2

from bot.base.common import ImageMatchConfig


class Template:
    template_name: str
    template_image: object
    resource_path: str
    image_match_config: ImageMatchConfig

    def __init__(self,
                 template_name: str,
                 resource_path: str,
                 image_match_config: ImageMatchConfig = ImageMatchConfig()):
        self.resource_path = resource_path
        self.template_name = template_name
        self.template_image = cv2.imread("resource" + self.resource_path + "/" + template_name.lower() + ".png", 0)
        self.image_match_config = image_match_config


class UI:
    ui_name = None
    check_exist_template_list: list[Template] = None
    check_non_exist_template_list: list[Template] = None

    def __init__(self, ui_name, check_exist_template_list: list[Template],
                 check_non_exist_template_list: list[Template]):
        self.ui_name = ui_name
        self.check_exist_template_list = check_exist_template_list
        self.check_non_exist_template_list = check_non_exist_template_list


NOT_FOUND_UI = UI("NOT_FOUND_UI", [], [])
