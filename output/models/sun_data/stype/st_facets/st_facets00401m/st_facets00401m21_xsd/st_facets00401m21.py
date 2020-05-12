from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A1:
    :cvar A2:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A6:
    :cvar VALUE_0:
    :cvar VALUE_00:
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_06:
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    """
    A0 = "Ῥa0"
    A1 = "Ώa1"
    A2 = "ↂa2"
    A3 = "ゔa3"
    A4 = "ヺa4"
    A5 = "ㄬa5"
    A6 = "힣a6"
    VALUE_0 = "Ὺ-0"
    VALUE_00 = "Ῠ00"
    VALUE_01 = "Ὸ01"
    VALUE_02 = "ↀ02"
    VALUE_03 = "ぁ03"
    VALUE_04 = "ァ04"
    VALUE_05 = "ㄅ05"
    VALUE_06 = "가06"
    VALUE_1 = "Ό-1"
    VALUE_2 = "ↁ-2"
    VALUE_3 = "な-3"
    VALUE_4 = "ネ-4"
    VALUE_5 = "ㄘ-5"
    VALUE_6 = "쇑-6"


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
