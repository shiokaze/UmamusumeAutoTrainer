import time
from enum import Enum
from abc import abstractmethod, ABCMeta
import random

import bot.base.log as logger
from bot.base.common import CronJobConfig
from bot.base.const import ALPHA

log = logger.get_logger(__name__)


class TaskExecuteMode(Enum):
    TASK_EXECUTE_MODE_INVALID = 0
    TASK_EXECUTE_MODE_ONE_TIME = 1
    TASK_EXECUTE_MODE_CRON_JOB = 2


class TaskStatus(Enum):
    TASK_STATUS_INVALID = 0
    TASK_STATUS_PENDING = 1
    TASK_STATUS_RUNNING = 2
    TASK_STATUS_INTERRUPT = 3
    TASK_STATUS_SUCCESS = 4
    TASK_STATUS_FAILED = 5
    TASK_STATUS_SCHEDULED = 6
    TASK_STATUS_CANCELED = 7


class EndTaskReason(Enum):
    COMPLETE = "任务已完成"
    MANUAL_ABORTED = "任务被手动中止"
    SYSTEM_ERROR = "系统异常"


class Task(metaclass=ABCMeta):
    task_id: str = None
    app_name: str = None
    task_execute_mode: TaskExecuteMode = None
    cron_job_config: CronJobConfig = None
    task_type = None
    task_status: TaskStatus = None
    task_desc: str = None
    task_start_time: int = None
    task_end_time: int = None
    end_task_reason: EndTaskReason = None

    def __init__(self, app_name: str, task_execute_mode: TaskExecuteMode, task_type,
                 task_desc: str, cron_job_config: CronJobConfig = None):
        self.task_id = "".join(random.sample(ALPHA, 5)) + str(int(time.time()))
        self.app_name = app_name
        self.task_execute_mode = task_execute_mode
        self.task_type = task_type
        if task_execute_mode == TaskExecuteMode.TASK_EXECUTE_MODE_CRON_JOB:
            self.task_status = TaskStatus.TASK_STATUS_SCHEDULED
        else:
            self.task_status = TaskStatus.TASK_STATUS_PENDING
        self.task_desc = task_desc
        self.cron_job_config = cron_job_config

    @abstractmethod
    def end_task(self, status, reason) -> None:
        log.info("任务结束：" + self.task_status.name + "->" + status.name)
        self.task_status = status
        self.end_task_reason = reason

    @abstractmethod
    def start_task(self) -> None:
        pass

    def running(self) -> bool:
        return self.task_status == TaskStatus.TASK_STATUS_RUNNING

