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

    aoharu_config: AoharuConfig = None
    
    def __init__(self, aoharu_config: AoharuConfig = None):
        self.aoharu_config = aoharu_config
