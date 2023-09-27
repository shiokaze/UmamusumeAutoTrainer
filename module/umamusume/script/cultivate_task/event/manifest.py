from typing import Union

from bot.recog.ocr import find_similar_text
from module.umamusume.context import UmamusumeContext
from module.umamusume.script.cultivate_task.event.scenario_event import scenario_event_1, scenario_event_2
import bot.base.log as logger

log = logger.get_logger(__name__)

event_map: dict[str, Union[callable, int]] = {
    "安心～针灸师，登☆场": 5,
    "新年的抱负": scenario_event_1,
    "新年参拜": scenario_event_2
}

event_name_list: list[str] = [*event_map]


def get_event_choice(ctx: UmamusumeContext, event_name: str) -> int:
    event_name = find_similar_text(event_name, event_name_list, 0.8)
    if event_name != "":
        if event_name in event_map:
            opt = event_map[event_name]
            if type(opt) is int:
                return opt
            if type(opt) is callable:
                return opt(ctx)
            else:
                log.warning("事件[%s]未提供处理逻辑", event_name)
                return 1
    log.debug("未知事件[%s]，使用默认选项1", event_name)
    return 1
