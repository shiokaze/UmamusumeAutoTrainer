from bot.base.manifest import APP_MANIFEST_LIST
from bot.engine.scheduler import scheduler


def start():
    scheduler.start()


def stop():
    scheduler.stop()


def add_task(app_name, task_execute_mode, task_type, task_desc, cron_job_config, attachment_data):
    app_config = APP_MANIFEST_LIST[app_name]
    task = app_config.build_task(task_execute_mode, task_type, task_desc, cron_job_config, attachment_data)
    scheduler.add_task(task)


def delete_task(task_id):
    scheduler.delete_task(task_id)


def get_task_list():
    return scheduler.get_task_list()


def reset_task(task_id):
    scheduler.reset_task(task_id)
