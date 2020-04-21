from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_MINUS_0:
    :cvar VALUE_00:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_MINUS_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_MINUS_2:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_MINUS_5:
    :cvar VALUE_05:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_MINUS_6:
    :cvar A6:
    :cvar VALUE_MINUS_7:
    :cvar VALUE_07:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_MINUS_8:
    :cvar A8:
    :cvar VALUE_MINUS_9:
    :cvar VALUE_09:
    :cvar A9:
    """
    VALUE_MINUS_0 = "এ-0"
    VALUE_00 = "এ00"
    A0 = "ঐa0"
    VALUE_01 = "ও01"
    VALUE_MINUS_1 = "ঝ-1"
    A1 = "নa1"
    VALUE_02 = "প02"
    VALUE_MINUS_2 = "ভ-2"
    A2 = "রa2"
    VALUE_03 = "ল03"
    VALUE_04 = "শ04"
    VALUE_MINUS_4 = "ষ-4"
    A4 = "হa4"
    VALUE_MINUS_5 = "ড়-5"
    VALUE_05 = "ড়05"
    A5 = "ঢ়a5"
    VALUE_06 = "য়06"
    VALUE_MINUS_6 = "ৠ-6"
    A6 = "ৡa6"
    VALUE_MINUS_7 = "ৰ-7"
    VALUE_07 = "ৰ07"
    A7 = "ৱa7"
    VALUE_08 = "ਅ08"
    VALUE_MINUS_8 = "ਇ-8"
    A8 = "ਊa8"
    VALUE_MINUS_9 = "ਏ-9"
    VALUE_09 = "ਏ09"
    A9 = "ਐa9"


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
