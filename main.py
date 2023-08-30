import threading

from bot.base.manifest import register_app
from bot.engine.scheduler import scheduler
from module.umamusume.manifest import UmamusumeManifest
from uvicorn import run

if __name__ == '__main__':
    register_app(UmamusumeManifest)
    scheduler_thread = threading.Thread(target=scheduler.init, args=())
    scheduler_thread.start()
    print("UAT running on http://127.0.0.1:8071")
    run("bot.server.handler:server", host="127.0.0.1", port=8071, log_level="error")

