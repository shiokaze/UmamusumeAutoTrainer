from module.umamusume.context import UmamusumeContext, UmamusumeTaskType
from module.umamusume.asset.point import *

NO_RP_RETRY_PENDING = 7200


def ts_script_main_menu(ctx: UmamusumeContext):
    if ctx.task.task_type == UmamusumeTaskType.UMAMUSUME_TASK_TYPE_TEAM_STADIUM:
        if not no_rp(ctx):
            ctx.ctrl.click_by_point(TO_RACE)
        else:
            from module.umamusume.task import EndTaskReason
            from bot.base.task import TaskStatus
            ctx.task.end_task(TaskStatus.TASK_STATUS_PENDING, EndTaskReason.RP_NOT_ENOUGH)


def script_race_home(ctx: UmamusumeContext):
    if ctx.task.task_type == UmamusumeTaskType.UMAMUSUME_TASK_TYPE_TEAM_STADIUM and not no_rp(ctx):
        ctx.ctrl.click_by_point(TO_TEAM_STADIUM)
    else:
        ctx.ctrl.click_by_point(GO_HOME_FROM_RACE)


def script_team_stadium_home(ctx: UmamusumeContext):
    if ctx.task.task_type == UmamusumeTaskType.UMAMUSUME_TASK_TYPE_TEAM_STADIUM and not no_rp(ctx):
        ctx.ctrl.click_by_point(TO_TEAM_RACE)
    else:
        ctx.ctrl.click_by_point(TEAM_STADIUM_RETURN)


def script_team_stadium_home_na(ctx: UmamusumeContext):
    from module.umamusume.task import EndTaskReason
    from bot.base.task import TaskStatus
    ctx.task.end_task(TaskStatus.TASK_STATUS_PENDING, EndTaskReason.OFF)


def script_team_stadium_select_opponent(ctx: UmamusumeContext):
    from .select_opponent import select_opponent
    match select_opponent(ctx):
        case 1:
            ctx.ctrl.click_by_point(TEAM_STADIUM_OPPO_UP)
        case 2:
            ctx.ctrl.click_by_point(TEAM_STADIUM_OPPO_MID)
        case 3:
            ctx.ctrl.click_by_point(TEAM_STADIUM_OPPO_DOWN)
        case 4:
            ctx.ctrl.click_by_point(TEAM_STADIUM_OPPO_REFRESH)


def script_team_stadium_before_race(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CONTINUE)


def script_team_stadium_select_item(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_RACE)


def script_team_stadium_check_all_results(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CHECK_RESULTS)


def script_team_stadium_check_result(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_SHORTEN)


def script_team_stadium_results(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CONTINUE)


def script_team_stadium_reward(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CLAIM_REWARDS)


def script_team_stadium_time_sale(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_TO_TIME_SALE)
    bought = ctx.task.detail.time_sale_bought
    if bought and bought[-1] or not bought:
        bought.append([])


def script_team_stadium_before_reward(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CHECK_RESULTS)


def script_team_stadium_end(ctx: UmamusumeContext):
    if no_rp(ctx):
        ctx.ctrl.click_by_point(TEAM_STADIUM_RETURN)
    else:
        ctx.ctrl.click_by_point(TEAM_STADIUM_RACE_AGAIN)


def script_team_stadium_no_rp(ctx: UmamusumeContext):
    import datetime
    ctx.task.detail.no_rp_timestamp = datetime.datetime.now().timestamp()
    ctx.ctrl.click_by_point(TEAM_STADIUM_CONFIRM_CANCEL)


def script_team_stadium_high_score(ctx: UmamusumeContext):
    ctx.ctrl.click_by_point(TEAM_STADIUM_CONTINUE)


def no_rp(ctx: UmamusumeContext):
    if not ctx.task.detail.no_rp_timestamp:
        return False
    import datetime
    return datetime.datetime.now().timestamp() - ctx.task.detail.no_rp_timestamp < NO_RP_RETRY_PENDING
