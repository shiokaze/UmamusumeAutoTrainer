from module.umamusume.context import UmamusumeContext
from module.umamusume.define import TurnOperationType


# 第一年新年事件
def scenario_event_1(ctx: UmamusumeContext) -> int:
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and ctx.cultivate_detail.turn_info.remain_stamina >= 50 or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and ctx.cultivate_detail.turn_info.remain_stamina >= 50:
        return 3
    else:
        return 2


# 第二年新年事件
def scenario_event_2(ctx: UmamusumeContext) -> int:
    if ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_REST or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_MEDIC and ctx.cultivate_detail.turn_info.remain_stamina >= 40 or \
            ctx.cultivate_detail.turn_info.turn_operation == TurnOperationType.TURN_OPERATION_TYPE_TRIP and ctx.cultivate_detail.turn_info.remain_stamina >= 50:
        return 3
    else:
        return 1
