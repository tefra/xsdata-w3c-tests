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
    :cvar A8:
    :cvar A9:
    :cvar VALUE_0:
    :cvar VALUE_00:
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_08:
    :cvar VALUE_09:
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "హa0"
    A1 = "ౡa1"
    A2 = "ಌa2"
    A3 = "ಐa3"
    A4 = "ನa4"
    A5 = "ಳa5"
    A6 = "ಹa6"
    A8 = "ೡa8"
    A9 = "ഌa9"
    VALUE_0 = "ష-0"
    VALUE_00 = "వ00"
    VALUE_01 = "ౠ01"
    VALUE_02 = "ಅ02"
    VALUE_03 = "ಎ03"
    VALUE_04 = "ಒ04"
    VALUE_05 = "ಪ05"
    VALUE_06 = "ವ06"
    VALUE_07 = "ೞ07"
    VALUE_08 = "ೠ08"
    VALUE_09 = "അ09"
    VALUE_1 = "ౠ-1"
    VALUE_2 = "ಈ-2"
    VALUE_3 = "ಏ-3"
    VALUE_4 = "ಝ-4"
    VALUE_5 = "ಮ-5"
    VALUE_6 = "ಷ-6"
    VALUE_8 = "ೠ-8"
    VALUE_9 = "ഈ-9"


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
