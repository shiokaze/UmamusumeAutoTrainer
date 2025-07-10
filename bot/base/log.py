import logging
import os
import sys
import time
import threading
from collections import deque
from logging import Logger
from bot.base.user_data import base_path
from bot.base.localization import localization
import colorlog

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
log_path = os.path.join(base_path, "log_" + current_time + ".txt")

class TaskLogHandler(logging.Handler):
    def __init__(self, capacity=1000):
        super().__init__()
        self.task_id = None
        self.buffer = {}
        self.lock = threading.RLock()
        self.capacity = capacity

    def emit(self, record):
        if hasattr(record, "task_id"):
            self.task_id = record.task_id
        if self.task_id is not None:
            if self.task_id not in self.buffer:
                self.buffer[self.task_id] = deque(maxlen=self.capacity)
            log_text = localization(self.format(record))
            with self.lock:
                self.buffer[self.task_id].append(log_text)

    def get_task_log(self, task_id):
        with self.lock:
            logs = list(self.buffer[task_id])
        return logs

task_log_handler = TaskLogHandler()
fmt = logging.Formatter('%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M')
task_log_handler.setFormatter(fmt)
task_log_handler.setLevel(logging.INFO)


def get_logger(name) -> Logger:
    logger = logging.getLogger(name)
    logger.propagate = False
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        fmt = colorlog.ColoredFormatter(
            fmt='%(log_color)s%(asctime)s  %(levelname)-8s [%(funcName)34s] %(filename)-20s: %(message)s',
            log_colors=log_colors_config
        )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(fmt)
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

        fmt = logging.Formatter('%(asctime)s  %(levelname)-8s [%(funcName)34s] %(filename)-20s: %(message)s') 
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(fmt)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        logger.addHandler(task_log_handler)
    return logger


