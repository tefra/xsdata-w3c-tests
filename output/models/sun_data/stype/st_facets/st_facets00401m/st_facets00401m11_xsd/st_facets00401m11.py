from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A1:
    :cvar A2:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A6:
    :cvar A7:
    :cvar A8:
    :cvar A9:
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
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A1 = "டa1"
    A2 = "தa2"
    A3 = "பa3"
    A4 = "வa4"
    A5 = "ஹa5"
    A6 = "ఌa6"
    A7 = "ఐa7"
    A8 = "నa8"
    A9 = "ళa9"
    VALUE_00 = "ஜ00"
    VALUE_01 = "ஞ01"
    VALUE_02 = "ண02"
    VALUE_03 = "ந03"
    VALUE_04 = "ம04"
    VALUE_05 = "ஷ05"
    VALUE_06 = "అ06"
    VALUE_07 = "ఎ07"
    VALUE_08 = "ఒ08"
    VALUE_09 = "ప09"
    VALUE_1 = "ஞ-1"
    VALUE_2 = "ண-2"
    VALUE_3 = "ன-3"
    VALUE_4 = "ற-4"
    VALUE_5 = "ஸ-5"
    VALUE_6 = "ఈ-6"
    VALUE_7 = "ఏ-7"
    VALUE_8 = "ఝ-8"
    VALUE_9 = "మ-9"


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
