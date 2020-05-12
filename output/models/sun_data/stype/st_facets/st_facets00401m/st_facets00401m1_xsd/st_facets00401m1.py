from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A01:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A6:
    :cvar A7:
    :cvar A8:
    :cvar A9:
    :cvar D_1:
    :cvar HA1:
    :cvar J02:
    :cvar M_0:
    :cvar R_2:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_08:
    :cvar VALUE_09:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    :cvar ZA0:
    :cvar ZA2:
    """
    A00 = "A00"
    A01 = "a01"
    A3 = "Öa3"
    A4 = "Þa4"
    A5 = "öa5"
    A6 = "ÿa6"
    A7 = "ıa7"
    A8 = "ľa8"
    A9 = "ňa9"
    D_1 = "d-1"
    HA1 = "ha1"
    J02 = "j02"
    M_0 = "M-0"
    R_2 = "r-2"
    VALUE_03 = "À03"
    VALUE_04 = "Ø04"
    VALUE_05 = "à05"
    VALUE_06 = "ø06"
    VALUE_07 = "Ā07"
    VALUE_08 = "Ĵ08"
    VALUE_09 = "Ł09"
    VALUE_3 = "Ë-3"
    VALUE_4 = "Û-4"
    VALUE_5 = "ë-5"
    VALUE_6 = "û-6"
    VALUE_7 = "Ę-7"
    VALUE_8 = "Ĺ-8"
    VALUE_9 = "ń-9"
    ZA0 = "Za0"
    ZA2 = "za2"


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
