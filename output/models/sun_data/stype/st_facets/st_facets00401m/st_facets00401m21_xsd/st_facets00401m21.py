from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_MINUS_0:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_MINUS_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_MINUS_2:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_MINUS_3:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_MINUS_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_MINUS_6:
    :cvar A6:
    """
    VALUE_00 = "Ῠ00"
    VALUE_MINUS_0 = "Ὺ-0"
    A0 = "Ῥa0"
    VALUE_01 = "Ὸ01"
    VALUE_MINUS_1 = "Ό-1"
    A1 = "Ώa1"
    VALUE_02 = "ↀ02"
    VALUE_MINUS_2 = "ↁ-2"
    A2 = "ↂa2"
    VALUE_03 = "ぁ03"
    VALUE_MINUS_3 = "な-3"
    A3 = "ゔa3"
    VALUE_04 = "ァ04"
    VALUE_MINUS_4 = "ネ-4"
    A4 = "ヺa4"
    VALUE_05 = "ㄅ05"
    VALUE_MINUS_5 = "ㄘ-5"
    A5 = "ㄬa5"
    VALUE_06 = "가06"
    VALUE_MINUS_6 = "쇑-6"
    A6 = "힣a6"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    value: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
