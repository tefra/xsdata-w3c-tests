from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_0:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_2:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_3:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_6:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_9:
    :cvar A9:
    """
    VALUE_00 = "Ӑ00"
    VALUE_0 = "ӝ-0"
    A0 = "ӫa0"
    VALUE_01 = "Ӯ01"
    VALUE_1 = "ӱ-1"
    A1 = "ӵa1"
    VALUE_02 = "Ӹ02"
    VALUE_2 = "Ӹ-2"
    A2 = "ӹa2"
    VALUE_03 = "Ա03"
    VALUE_3 = "Ճ-3"
    A3 = "Ֆa3"
    VALUE_04 = "ՙ04"
    VALUE_05 = "ա05"
    VALUE_5 = "ճ-5"
    A5 = "ֆa5"
    VALUE_06 = "א06"
    VALUE_6 = "ם-6"
    A6 = "תa6"
    VALUE_07 = "װ07"
    VALUE_7 = "ױ-7"
    A7 = "ײa7"
    VALUE_08 = "ء08"
    VALUE_8 = "ح-8"
    A8 = "غa8"
    VALUE_09 = "ف09"
    VALUE_9 = "م-9"
    A9 = "يa9"


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
