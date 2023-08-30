import subprocess
from subprocess import Popen
from typing import Any
from plyer import notification
import bot.base.log as logger

log = logger.get_logger(__name__)


# run_cmd 执行命令行
def run_cmd(cmd_string) -> Popen[bytes] | Popen[Any]:
    log.debug('run cmdline: {}'.format(cmd_string))
    return subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def push_system_notification(title, message, timeout):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout
    )
