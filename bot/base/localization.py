class LocalizationMap:
    SCENARIO_TYPE_UNKNOWN = '未知'
    SCENARIO_TYPE_URA = 'URA'
    SCENARIO_TYPE_AOHARUHAI = '青春杯'

    SUPPORT_CARD_TYPE_UNKNOWN = '未知'
    SUPPORT_CARD_TYPE_SPEED = '速度'
    SUPPORT_CARD_TYPE_STAMINA = '耐力'
    SUPPORT_CARD_TYPE_POWER = '力量'
    SUPPORT_CARD_TYPE_WILL = '毅力'
    SUPPORT_CARD_TYPE_INTELLIGENCE = '智力'
    SUPPORT_CARD_TYPE_FRIEND = '友情'
    SUPPORT_CARD_TYPE_GROUP = '团队'
    SUPPORT_CARD_TYPE_NPC = 'NPC'

    SUPPORT_CARD_FAVOR_LEVEL_UNKNOWN = '未知'
    SUPPORT_CARD_FAVOR_LEVEL_1 = '等级1'
    SUPPORT_CARD_FAVOR_LEVEL_2 = '等级2'
    SUPPORT_CARD_FAVOR_LEVEL_3 = '等级3'
    SUPPORT_CARD_FAVOR_LEVEL_4 = '等级4'

    TRAINING_TYPE_UNKNOWN = '未知'
    TRAINING_TYPE_SPEED = '速度'
    TRAINING_TYPE_STAMINA = '耐力'
    TRAINING_TYPE_POWER = '力量'
    TRAINING_TYPE_WILL = '毅力'
    TRAINING_TYPE_INTELLIGENCE = '智力'

    MOTIVATION_LEVEL_UNKNOWN = '未知'
    MOTIVATION_LEVEL_1 = '等级1'
    MOTIVATION_LEVEL_2 = '等级2'
    MOTIVATION_LEVEL_3 = '等级3'
    MOTIVATION_LEVEL_4 = '等级4'
    MOTIVATION_LEVEL_5 = '等级5'

    TURN_OPERATION_TYPE_UNKNOWN = '未知'
    TURN_OPERATION_TYPE_TRAINING = '训练'
    TURN_OPERATION_TYPE_REST = '休息'
    TURN_OPERATION_TYPE_MEDIC = '医务室'
    TURN_OPERATION_TYPE_TRIP = '外出'
    TURN_OPERATION_TYPE_RACE = '赛事'

    SUPPORT_CARD_UMA_UNKNOWN = '未知'
    SUPPORT_CARD_UMA_AKIKAWA = '理事长'
    SUPPORT_CARD_UMA_REPORTER = '记者'

    RACE_TACTIC_TYPE_UNKNOWN = '未知'
    RACE_TACTIC_TYPE_BACK = '后追'
    RACE_TACTIC_TYPE_MIDDLE = '居中'
    RACE_TACTIC_TYPE_FRONT = '跟前'
    RACE_TACTIC_TYPE_ESCAPE = '领跑'

    TASK_STATUS_INVALID = '任务无效'
    TASK_STATUS_PENDING = '任务暂停'
    TASK_STATUS_RUNNING = '任务运行'
    TASK_STATUS_INTERRUPT = '任务被打断'
    TASK_STATUS_SUCCESS = '任务完成'
    TASK_STATUS_FAILED = '任务失败'
    TASK_STATUS_SCHEDULED = '任务定时'
    TASK_STATUS_CANCELED = '任务取消'

    support_card = '暂无'

localization_map = {attr: value for attr, value in vars(LocalizationMap).items()
                    if not callable(value) and not attr.startswith('_')}

def _localization_single(string):
    for name, value in localization_map.items():
        string = string.replace(name, value)
    return string


def localization(text):
    if isinstance(text, str):
        return _localization_single(text)
    if not isinstance(text, list):
        raise TypeError(f'localization failed: illegal type {type(text)}')
    for i, string in enumerate(text):
        if not isinstance(string, str):
            raise TypeError(f'localization failed: illegal type {type(string)}')
        text[i] = _localization_single(string)
    return text
