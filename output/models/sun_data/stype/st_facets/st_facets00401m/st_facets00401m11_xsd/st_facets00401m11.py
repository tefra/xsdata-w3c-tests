from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_MINUS_1:
    :cvar VALUE_01:
    :cvar A1:
    :cvar VALUE_MINUS_2:
    :cvar VALUE_02:
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
    VALUE_00 = "ஜ00"
    VALUE_MINUS_1 = "ஞ-1"
    VALUE_01 = "ஞ01"
    A1 = "டa1"
    VALUE_MINUS_2 = "ண-2"
    VALUE_02 = "ண02"
    A2 = "தa2"
    VALUE_03 = "ந03"
    VALUE_MINUS_3 = "ன-3"
    A3 = "பa3"
    VALUE_04 = "ம04"
    VALUE_MINUS_4 = "ற-4"
    A4 = "வa4"
    VALUE_05 = "ஷ05"
    VALUE_MINUS_5 = "ஸ-5"
    A5 = "ஹa5"
    VALUE_06 = "అ06"
    VALUE_MINUS_6 = "ఈ-6"
    A6 = "ఌa6"
    VALUE_07 = "ఎ07"
    VALUE_MINUS_7 = "ఏ-7"
    A7 = "ఐa7"
    VALUE_08 = "ఒ08"
    VALUE_MINUS_8 = "ఝ-8"
    A8 = "నa8"
    VALUE_09 = "ప09"
    VALUE_MINUS_9 = "మ-9"
    A9 = "ళa9"


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
