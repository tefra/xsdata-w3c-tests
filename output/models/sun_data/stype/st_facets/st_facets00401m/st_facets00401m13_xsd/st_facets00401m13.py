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
    :cvar A6:
    :cvar A7:
    :cvar A8:
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
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    """
    A0 = "ഐa0"
    A1 = "നa1"
    A2 = "ഹa2"
    A3 = "ൡa3"
    A4 = "ฮa4"
    A6 = "ำa6"
    A7 = "ๅa7"
    A8 = "ຂa8"
    VALUE_0 = "ഏ-0"
    VALUE_00 = "എ00"
    VALUE_01 = "ഒ01"
    VALUE_02 = "പ02"
    VALUE_03 = "ൠ03"
    VALUE_04 = "ก04"
    VALUE_05 = "ะ05"
    VALUE_06 = "า06"
    VALUE_07 = "เ07"
    VALUE_08 = "ກ08"
    VALUE_09 = "ຄ09"
    VALUE_1 = "ഝ-1"
    VALUE_2 = "റ-2"
    VALUE_3 = "ൠ-3"
    VALUE_4 = "ท-4"
    VALUE_6 = "า-6"
    VALUE_7 = "โ-7"
    VALUE_8 = "ກ-8"


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
