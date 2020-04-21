from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar M_0:
    :cvar ZA0:
    :cvar A01:
    :cvar D_1:
    :cvar HA1:
    :cvar J02:
    :cvar R_2:
    :cvar ZA2:
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
    :cvar VALUE_07:
    :cvar VALUE_MINUS_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_MINUS_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_MINUS_9:
    :cvar A9:
    """
    A00 = "A00"
    M_0 = "M-0"
    ZA0 = "Za0"
    A01 = "a01"
    D_1 = "d-1"
    HA1 = "ha1"
    J02 = "j02"
    R_2 = "r-2"
    ZA2 = "za2"
    VALUE_03 = "À03"
    VALUE_MINUS_3 = "Ë-3"
    A3 = "Öa3"
    VALUE_04 = "Ø04"
    VALUE_MINUS_4 = "Û-4"
    A4 = "Þa4"
    VALUE_05 = "à05"
    VALUE_MINUS_5 = "ë-5"
    A5 = "öa5"
    VALUE_06 = "ø06"
    VALUE_MINUS_6 = "û-6"
    A6 = "ÿa6"
    VALUE_07 = "Ā07"
    VALUE_MINUS_7 = "Ę-7"
    A7 = "ıa7"
    VALUE_08 = "Ĵ08"
    VALUE_MINUS_8 = "Ĺ-8"
    A8 = "ľa8"
    VALUE_09 = "Ł09"
    VALUE_MINUS_9 = "ń-9"
    A9 = "ňa9"


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
