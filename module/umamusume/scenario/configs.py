class UraConfig:
    skill_event_weight: list[int]
    reset_skill_event_weight_list: list[str]

    def __init__(self, config: dict):
        if "skillEventWeight" not in config or "resetSkillEventWeightList" not in config:
            raise ValueError("错误的配置: 必须配置 'skillEventWeight' 和 'resetSkillEventWeightList'")
        self.skill_event_weight = config["skillEventWeight"]
        self.reset_skill_event_weight_list = config["resetSkillEventWeightList"]
    
    def removeSkillFromList(self, skill: str):
        if skill in self.reset_skill_event_weight_list:
            self.reset_skill_event_weight_list.remove(skill)
            # 如果技能列表空了, 重置权重
            # 如果一开始列表就是空的, 这个分支就不会触发, 也不会重置权重
            if len(self.reset_skill_event_weight_list) == 0:
                self.skill_event_weight = [0, 0, 0]
    
    def getSkillEventWeight(self, date: int) -> int:
        if date <= 24:
            return self.skill_event_weight[0]
        elif date <= 48:
            return self.skill_event_weight[1]
        else:
            return self.skill_event_weight[2]

class AoharuConfig:

    preliminary_round_selections: list[int]
    aoharu_team_name_selection: int

    def __init__(self, config: dict):
        if "preliminaryRoundSelections" not in config or "aoharuTeamNameSelection" not in config:
            raise ValueError("错误的配置: 必须配置 'preliminaryRoundSelections' 和 'aoharuTeamNameSelection'")
        self.preliminary_round_selections = config["preliminaryRoundSelections"]
        self.aoharu_team_name_selection = config["aoharuTeamNameSelection"]

    def get_opponent(self, round_index: int) -> int:
        """ 获取指定轮次的对手索引, 索引从0开始, 预赛第一轮为0 """
        if round_index < 0 or round_index >= len(self.preliminary_round_selections):
            raise IndexError("轮次索引超出范围")
        return self.preliminary_round_selections[round_index]
    
class ScenarioConfig:
    """ 所有场景的配置 """
    ura_config: UraConfig = None
    aoharu_config: AoharuConfig = None
    
    def __init__(self, ura_config: UraConfig = None, aoharu_config: AoharuConfig = None):
        self.ura_config = ura_config
        self.aoharu_config = aoharu_config
