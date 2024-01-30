import threading
import time
import traceback
import psutil

import bot.base.log as logger
import cv2

from bot.base.common import ImageMatchMode
from bot.base.resource import UI, NOT_FOUND_UI
from bot.base.task import TaskStatus, Task, EndTaskReason
from bot.conn.os import push_system_notification
from bot.conn.u2_ctrl import U2AndroidController
from bot.recog.image_matcher import template_match
from concurrent.futures import ThreadPoolExecutor
from bot.base.manifest import APP_MANIFEST_LIST
from config import CONFIG


log = logger.get_logger(__name__)

debug = True


def get_controller() -> U2AndroidController:
    return U2AndroidController()


class Executor:
    active = True

    app_alive_check_counter = 5
    app_alive_check_interval = 5

    detect_ui_results_write_lock = threading.Lock()
    detect_ui_results = []
    executor = ThreadPoolExecutor(max_workers=CONFIG.bot.auto.cpu_alloc)

    def __init__(self):
        psutil.Process().cpu_affinity(list(range(CONFIG.bot.auto.cpu_alloc)))
        pass

    def start(self, task):
        self.active = True
        self.run_work_flow(task)

    def stop(self):
        self.active = False

    def detect_ui(self, ui_list: list[UI], target) -> UI:
        # start_time = time.time()
        target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        futures = []
        for ui in ui_list:
            future = self.executor.submit(self.detect_ui_sub, ui, target)
            futures.append(future)
        for future in futures:
            future.result()
        # end_time = time.time()
        # log.debug("detect ui cost: " + str(end_time - start_time))
        if len(self.detect_ui_results) > 0:
            result = self.detect_ui_results[0]
            self.detect_ui_results = []
            return result
        else:
            return NOT_FOUND_UI

    def detect_ui_sub(self, ui: UI, target) -> None:
        result = True
        for template in ui.check_exist_template_list:
            sub_target = target[
                         template.image_match_config.match_area.y1:template.image_match_config.match_area.y2,
                         template.image_match_config.match_area.x1:template.image_match_config.match_area.x2]
            if template.image_match_config.match_mode == ImageMatchMode.IMAGE_MATCH_MODE_TEMPLATE_MATCH:
                if not template_match(sub_target, template.template_image).find_match:
                    result = False
                    break
            else:
                log.error("template not set match mode")
        for template in ui.check_non_exist_template_list:
            sub_target = target[
                         template.image_match_config.match_area.y1:template.image_match_config.match_area.y2,
                         template.image_match_config.match_area.x1:template.image_match_config.match_area.x2]
            if template.image_match_config.match_mode == ImageMatchMode.IMAGE_MATCH_MODE_TEMPLATE_MATCH:
                if template_match(sub_target, template.template_image).find_match:
                    result = False
                    break
            else:
                log.error("template not set match mode")
        if result is True:
            self.detect_ui_results_write_lock.acquire()
            self.detect_ui_results.append(ui)
            self.detect_ui_results_write_lock.release()

    def run_work_flow(self, task: Task):
        manifest = APP_MANIFEST_LIST[task.app_name]
        ui_list = manifest.ui_list
        before_hook = manifest.before_hook
        after_hook = manifest.after_hook
        controller = get_controller()
        try:
            # 初始化
            if hasattr(task, 'device_name') and task.device_name:
                from bot.conn.u2_ctrl import U2AndroidConfig
                controller.config = U2AndroidConfig(_device_name=task.device_name,
                                                    delay=controller.config.delay,
                                                    bluestacks_config_path=controller.config.bluestacks_config_path,
                                                    bluestacks_config_keyword=
                                                    controller.config.bluestacks_config_keyword)
            controller.init_env()
            ctx = manifest.build_context(task, controller)
            ctx.ctrl = controller

            task.task_status = TaskStatus.TASK_STATUS_RUNNING
            task.start_task()
            task.task_start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            # 启动应用
            log.debug("启动："+manifest.app_package_name)
            ctx.ctrl.start_app(manifest.app_package_name)
            while self.active:
                if task.task_status == TaskStatus.TASK_STATUS_RUNNING:
                    ctx.current_screen = ctx.ctrl.get_screen()
                    if ctx.current_screen is None:
                        log.debug("未检测到图像")
                        time.sleep(1)
                        continue
                    ctx.prev_ui = ctx.current_ui
                    ctx.current_ui = self.detect_ui(ui_list, ctx.current_screen)
                    log.debug("current_ui:" + ctx.current_ui.ui_name)
                    if before_hook is not None:
                        before_hook(ctx)
                    manifest.script(ctx)
                    if after_hook is not None:
                        after_hook(ctx)
                    if ctx.is_task_finish():
                        task.end_task(TaskStatus.TASK_STATUS_SUCCESS, EndTaskReason.COMPLETE)
                else:
                    break
                time.sleep(0.5)
        except Exception:
            task.end_task(TaskStatus.TASK_STATUS_FAILED, EndTaskReason.SYSTEM_ERROR)
            traceback.print_exc()
        if not self.active:
            task.end_task(TaskStatus.TASK_STATUS_INTERRUPT, EndTaskReason.MANUAL_ABORTED)
        else:
            self.active = False
        task.end_task_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        push_system_notification("任务结束", str(task.end_task_reason.value), 10)
        controller.destroy()

