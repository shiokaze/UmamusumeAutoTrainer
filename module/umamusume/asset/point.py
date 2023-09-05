from bot.base.common import Coordinate
from bot.base.point import ClickPoint, ClickPointType
from module.umamusume.asset.template import *

# cultivate
TO_CULTIVATE_SCENARIO_CHOOSE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(545, 1085), "前往剧本选择", None)
TO_CULTIVATE_PREPARE_NEXT = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(355, 1080), "育成准备-前往下一步")
CULTIVATE_FINAL_CHECK_START = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(500, 1185), "开始育成")
TO_FOLLOW_SUPPORT_CARD_SELECT = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(570, 680), "借用支援卡")
FOLLOW_SUPPORT_CARD_SELECT_REFRESH = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(650, 1010), "借用支援卡-刷新")

TO_TRAINING_SELECT = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(355, 990), "前往训练选择", None)
CULTIVATE_REST = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(120, 995), "休息", None)
CULTIVATE_SKILL_LEARN = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(600, 987), "技能", None)
CULTIVATE_MEDIC = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(170, 1120), "保健室", None)
CULTIVATE_MEDIC_SUMMER = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(260, 1120), "保健室-夏合宿", None)
CULTIVATE_TRIP = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(355, 1130), "外出", None)
CULTIVATE_RACE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(564, 1127), "比赛", None)
CULTIVATE_RACE_SUMMER = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(460, 1125), "比赛-夏合宿", None)

RETURN_TO_CULTIVATE_MAIN_MENU = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(90, 1230), "返回训练主界面", None)
CULTIVATE_GOAL_RACE_INTER_1 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(508, 1081), "进入生涯赛详细界面", None)
CULTIVATE_GOAL_RACE_INTER_2 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360,1082), "开始生涯赛", None)
CULTIVATE_GOAL_RACE_INTER_3 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(520,920), "开始生涯赛-确认", None)

BEFORE_RACE_CHANGE_TACTIC = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(575, 745), "比赛前-更改战术", None)
BEFORE_RACE_CHANGE_TACTIC_4 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(585, 780), "更改战术-领跑", None)
BEFORE_RACE_CHANGE_TACTIC_3 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(435, 780), "更改战术-跟前", None)
BEFORE_RACE_CHANGE_TACTIC_2 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(285, 780), "更改战术-居中", None)
BEFORE_RACE_CHANGE_TACTIC_1 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(125, 780), "更改战术-后追", None)
TACTIC_LIST = [BEFORE_RACE_CHANGE_TACTIC_1, BEFORE_RACE_CHANGE_TACTIC_2, BEFORE_RACE_CHANGE_TACTIC_3, BEFORE_RACE_CHANGE_TACTIC_4]

BEFORE_RACE_CHANGE_TACTIC_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(515, 920), "更改战术-确认", None)
BEFORE_RACE_START = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(465, 1175), "比赛前-开始比赛", None)
BEFORE_RACE_SKIP = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(255, 1175), "比赛前-跳过比赛", None)
IN_RACE_UMA_LIST_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360,1175), "比赛马娘列表-确认", None)

IN_RACE_SKIP = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(560,1225), "比赛中-跳过", None)
SKIP = ClickPoint(ClickPointType.CLICK_POINT_TYPE_TEMPLATE, BTN_SKIP, None, "跳过", None)
SCENARIO_SKIP_OFF = ClickPoint(ClickPointType.CLICK_POINT_TYPE_TEMPLATE, BTN_SKIP_OFF, None, "跳过", None)
SCENARIO_SKIP_SPEED_1 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_TEMPLATE, BTN_SKIP_SPEED_1, None, "跳过", None)

SCENARIO_SHORTEN_SET_2 = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(350,630), "事件缩短设定-全部", None)
SCENARIO_SHORTEN_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360,925), "事件缩短设定-确认", None)
CULTIVATE_CATCH_DOLL_START = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(365,1117), "抓娃娃机-开始", None)
CULTIVATE_CATCH_DOLL_RESULT_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(365,1185), "抓娃娃机-结果确认", None)

RACE_RESULT_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(370,1150), "比赛结果-确认", None)
RACE_REWARD_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(520,1195), "比赛奖励-确认", None)
GOAL_ACHIEVE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(370,1110), "目标达成-确认", None)
GOAL_FAIL_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(370,1190), "目标未达成-确认", None)
NEXT_GOAL_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360,1110), "下一个目标-确认", None)

CULTIVATE_EXTEND_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360,915), "因子继承-确认", None)

TRAINING_SELECT_SPEED = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(105, 1085), "训练-速度", None)
TRAINING_SELECT_STAMINA = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(235, 1085), "训练-耐力", None)
TRAINING_SELECT_POWER = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 1085), "训练-力量", None)
TRAINING_SELECT_WILL = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(490, 1085), "训练-毅力", None)
TRAINING_SELECT_INTELLIGENCE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(620, 1085), "训练-智力", None)

TRAINING_POINT_LIST = [TRAINING_SELECT_SPEED, TRAINING_SELECT_STAMINA, TRAINING_SELECT_POWER,
                       TRAINING_SELECT_WILL, TRAINING_SELECT_INTELLIGENCE]

INFO_SUMMER_REST_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(520,835), "休息-夏合宿-确认", None)
NETWORK_ERROR_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(520,835), "网络异常-确认", None)
SKIP_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(520,835), "跳过-确认", None)
CULTIVATE_OPERATION_COMMON_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(520, 835), "育成操作通用确认", None)
RACE_RECOMMEND_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(365, 1185), "赛事推荐功能确认", None)
CULTIVATE_TRIP_WITH_FRIEND = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(370, 455), "外出旅行-选择友人", None)
RACE_FAIL_CONTINUE_USE_CLOCK = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(520,905), "使用闹钟-确认", None)
RACE_FAIL_CONTINUE_CANCEL = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(200,905), "使用闹钟-取消", None)
CULTIVATE_RECEIVE_CUP_CLOSE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(365,920), "获得奖杯-关闭", None)

CULTIVATE_FINISH_LEARN_SKILL = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(215, 1050), "育成完成-学习技能", None)
CULTIVATE_FINISH_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(512,1050), "育成完成-确认", None)
CULTIVATE_FINISH_CONFIRM_AGAIN = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(520,924), "育成完成-再次确认（放弃剩余技能pt）", None)


GET_TITLE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(350,1195), "获取称号-确认", None)
CULTIVATE_RESULT_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(360,1185), "育成结果-确认", None)
CULTIVATE_FINISH_RETURN_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(190, 835), "育成结束-返回", None)
CULTIVATE_LEARN_SKILL_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(360,1082), "技能学习-确认", None)
CULTIVATE_LEARN_SKILL_CONFIRM_AGAIN = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(530,1190), "技能学习-再次确认", None)
CULTIVATE_LEARN_SKILL_DONE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE,None, Coordinate(359,832), "技能学习-再次确认", None)
RETURN_TO_CULTIVATE_FINISH = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(90, 1190), "返回育成界面", None)

CULTIVATE_FAN_NOT_ENOUGH_RETURN = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(200, 915), "目标粉丝数不足-返回", None)
CULTIVATE_TOO_MUCH_RACE_WARNING_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(525, 840), "连续参赛-确认", None)

CULTIVATE_LEVEL_RESULT_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 1175), "养成等级-下一页", None)
CULTIVATE_FACTOR_RECEIVE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 1175), "因子获取-下一页", None)
HISTORICAL_RATING_UPDATE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 1115), "历代评分更新-下一页", None)
SCENARIO_RATING_UPDATE_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 1115), "历代评分更新-下一页", None)

RECEIVE_GIFT = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(515, 1180), "礼物箱-一键领取", None)
RECEIVE_GIFT_SUCCESS_CLOSE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_TEMPLATE, BTN_CLOSE, None, "礼物箱-领取成功-关闭", None)
UNLOCK_STORY_TO_HOME_PAGE = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 835), "解锁角色剧情-前往主页", None)
WIN_TIMES_NOT_ENOUGH_RETURN = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(200, 915), "目标达成次数不足-返回", None)
ACTIVITY_STORY_UNLOCK_CONFIRM = ClickPoint(ClickPointType.CLICK_POINT_TYPE_COORDINATE, None, Coordinate(360, 830), "活动剧情解锁-关闭", None)

