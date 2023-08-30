from bot.base.resource import UI
from typing import Dict


class AppManifest:

    app_name: str = None
    app_activity_name: str = None
    app_package_name: str = None
    build_context: callable = None
    build_task: callable = None
    ui_list: list[UI] = None
    script: callable = None
    before_hook: callable = None
    after_hook: callable = None

    def __init__(self, app_name: str, app_activity_name: str, app_package_name: str,
                 build_context: callable, build_task: callable, ui_list: list[UI],
                 script: callable, before_hook: callable, after_hook: callable):
        self.app_name = app_name
        self.app_activity_name = app_activity_name
        self.app_package_name = app_package_name
        self.build_context = build_context
        self.build_task = build_task
        self.ui_list = ui_list
        self.before_hook = before_hook
        self.after_hook = after_hook
        self.script = script


APP_MANIFEST_LIST: Dict[str, AppManifest] = {}


def register_app(app_manifest: AppManifest):
    APP_MANIFEST_LIST[app_manifest.app_name] = app_manifest
