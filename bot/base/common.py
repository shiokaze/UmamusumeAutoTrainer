from enum import Enum


class Area:

    x1: int = None
    y1: int = None
    x2: int = None
    y2: int = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class ImageMatchMode(Enum):
    IMAGE_MATCH_MODE_TEMPLATE_MATCH = 0
    IMAGE_MATCH_MODE_FEATURE_MATCH = 1


class ImageMatchConfig:
    match_area: Area
    match_mode: ImageMatchMode
    match_accuracy: float

    def __init__(self, match_area: Area = Area(0, 0, 720, 1280),
                 match_mode: ImageMatchMode = ImageMatchMode.IMAGE_MATCH_MODE_TEMPLATE_MATCH,
                 match_accuracy: float = 0.9):
        self.match_area = match_area
        self.match_mode = match_mode
        self.match_accuracy = match_accuracy


class Coordinate:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y


class CronJobConfig:
    cron = None
    next_time = None
    last_time = None


class CronConfig:
    cron = None
    times = None

    def __init__(self, cron, times):
        self.cron = cron
        self.times = times