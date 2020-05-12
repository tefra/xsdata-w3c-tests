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
    :cvar A5:
    :cvar A6:
    :cvar A7:
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
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ӫa0"
    A1 = "ӵa1"
    A2 = "ӹa2"
    A3 = "Ֆa3"
    A5 = "ֆa5"
    A6 = "תa6"
    A7 = "ײa7"
    A8 = "غa8"
    A9 = "يa9"
    VALUE_0 = "ӝ-0"
    VALUE_00 = "Ӑ00"
    VALUE_01 = "Ӯ01"
    VALUE_02 = "Ӹ02"
    VALUE_03 = "Ա03"
    VALUE_04 = "ՙ04"
    VALUE_05 = "ա05"
    VALUE_06 = "א06"
    VALUE_07 = "װ07"
    VALUE_08 = "ء08"
    VALUE_09 = "ف09"
    VALUE_1 = "ӱ-1"
    VALUE_2 = "Ӹ-2"
    VALUE_3 = "Ճ-3"
    VALUE_5 = "ճ-5"
    VALUE_6 = "ם-6"
    VALUE_7 = "ױ-7"
    VALUE_8 = "ح-8"
    VALUE_9 = "م-9"


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
