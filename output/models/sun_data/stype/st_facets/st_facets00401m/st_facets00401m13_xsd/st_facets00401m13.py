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
    :cvar VALUE_MINUS_3:
    :cvar VALUE_03:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_MINUS_6:
    :cvar VALUE_06:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_MINUS_7:
    :cvar A7:
    :cvar VALUE_MINUS_8:
    :cvar VALUE_08:
    :cvar A8:
    :cvar VALUE_09:
    """
    VALUE_00 = "എ00"
    VALUE_MINUS_0 = "ഏ-0"
    A0 = "ഐa0"
    VALUE_01 = "ഒ01"
    VALUE_MINUS_1 = "ഝ-1"
    A1 = "നa1"
    VALUE_02 = "പ02"
    VALUE_MINUS_2 = "റ-2"
    A2 = "ഹa2"
    VALUE_MINUS_3 = "ൠ-3"
    VALUE_03 = "ൠ03"
    A3 = "ൡa3"
    VALUE_04 = "ก04"
    VALUE_MINUS_4 = "ท-4"
    A4 = "ฮa4"
    VALUE_05 = "ะ05"
    VALUE_MINUS_6 = "า-6"
    VALUE_06 = "า06"
    A6 = "ำa6"
    VALUE_07 = "เ07"
    VALUE_MINUS_7 = "โ-7"
    A7 = "ๅa7"
    VALUE_MINUS_8 = "ກ-8"
    VALUE_08 = "ກ08"
    A8 = "ຂa8"
    VALUE_09 = "ຄ09"


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
