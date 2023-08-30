from abc import ABCMeta

from bot.base.point import ClickPoint


class AndroidController(metaclass=ABCMeta):

    def init_env(self):
        pass

    def click_by_point(self, point: ClickPoint):
        pass

    def click(self, x, y, name):
        pass

    def swipe(self, x1, y1, x2, y2, duration, name):
        pass

    def destroy(self):
        pass

    def start_app(self, name):
        pass

    def stop_app(self):
        pass

    def get_screen(self, to_gray=False):
        pass


