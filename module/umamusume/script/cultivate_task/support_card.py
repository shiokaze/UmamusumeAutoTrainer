from module.umamusume.context import SupportCardInfo, TurnInfo, UmamusumeContext
from module.umamusume.define import TrainingType, SupportCardType, SupportCardFavorLevel

DEFAULT = 0


def get_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo):
    if info.name in SCORE_DICT[info.card_type]:
        score = SCORE_DICT[info.card_type][info.name](ctx, info)
    else:
        score = SCORE_DICT[info.card_type][DEFAULT](ctx, info)
    return score


def default_speed_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_stamina_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_power_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_will_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_intelligence_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_friend_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1.5


def default_npc_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_group_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 1


def default_unknown_support_card_score(ctx: UmamusumeContext, info: SupportCardInfo) -> float:
    if (info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_3 or
            info.favor == SupportCardFavorLevel.SUPPORT_CARD_FAVOR_LEVEL_4):
        return 0.1
    return 0.5


SCORE_DICT: dict = {
    SupportCardType.SUPPORT_CARD_TYPE_SPEED: {
        DEFAULT: default_speed_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_STAMINA: {
        DEFAULT: default_stamina_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_POWER: {
        DEFAULT: default_power_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_WILL: {
        DEFAULT: default_will_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_INTELLIGENCE: {
        DEFAULT: default_intelligence_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_FRIEND: {
        DEFAULT: default_friend_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_NPC: {
        DEFAULT: default_npc_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_GROUP: {
        DEFAULT: default_group_support_card_score
    },
    SupportCardType.SUPPORT_CARD_TYPE_UNKNOWN: {
        DEFAULT: default_unknown_support_card_score
    },
}


