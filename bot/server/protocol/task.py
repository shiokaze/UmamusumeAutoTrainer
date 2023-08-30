from typing import Union
from pydantic import BaseModel

from bot.base.task import TaskExecuteMode


# 添加任务
class AddTaskRequest(BaseModel):
    app_name: str
    task_execute_mode: TaskExecuteMode
    task_type: int
    task_desc: str
    attachment_data: object
    cron_job_config: Union[object, None] = None


class AddTaskResponse(BaseModel):
    ret: int
    msg: str


# 删除任务
class DeleteTaskRequest(BaseModel):
    task_id: str


class DeleteTaskResponse(BaseModel):
    ret: int
    msg: str


# 重置任务
class ResetTaskRequest(BaseModel):
    task_id: str


