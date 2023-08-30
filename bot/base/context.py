from abc import abstractmethod, ABCMeta

from bot.base.resource import UI
from bot.base.task import Task
from bot.conn.ctrl import AndroidController


class BotContext(metaclass=ABCMeta):

    task: Task = None
    ctrl: AndroidController = None
    current_screen = None
    prev_ui: UI = None
    current_ui: UI = None

    next_ui: UI = None

    def __init__(self, task: Task, ctrl: AndroidController):
        self.task = task
        self.ctrl = ctrl

    @abstractmethod
    def is_task_finish(self) -> bool:
        pass


