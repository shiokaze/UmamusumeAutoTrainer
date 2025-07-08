import logging
import os
import sys
import time
from logging import Logger
from bot.base.user_data import base_path

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
task_logs = {}

class TaskLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.task_id = None

    def emit(self, record):
        if hasattr(record, "task_id"):
            self.task_id = record.task_id
        if self.task_id is not None:
            if self.task_id not in task_logs:
                task_logs[self.task_id] = []
            log_text = self.format(record)
            task_logs[self.task_id].append(log_text)


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

        fmt = logging.Formatter('%(asctime)s  %(levelname)-8s: %(message)s')
        task_log_handler = TaskLogHandler()
        task_log_handler.setFormatter(fmt)
        task_log_handler.setLevel(logging.INFO)
        logger.addHandler(task_log_handler)
    return logger


