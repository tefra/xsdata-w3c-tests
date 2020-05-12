from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A1:
    :cvar A2:
    :cvar A4:
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
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ঐa0"
    A1 = "নa1"
    A2 = "রa2"
    A4 = "হa4"
    A5 = "ঢ়a5"
    A6 = "ৡa6"
    A7 = "ৱa7"
    A8 = "ਊa8"
    A9 = "ਐa9"
    VALUE_0 = "এ-0"
    VALUE_00 = "এ00"
    VALUE_01 = "ও01"
    VALUE_02 = "প02"
    VALUE_03 = "ল03"
    VALUE_04 = "শ04"
    VALUE_05 = "ড়05"
    VALUE_06 = "য়06"
    VALUE_07 = "ৰ07"
    VALUE_08 = "ਅ08"
    VALUE_09 = "ਏ09"
    VALUE_1 = "ঝ-1"
    VALUE_2 = "ভ-2"
    VALUE_4 = "ষ-4"
    VALUE_5 = "ড়-5"
    VALUE_6 = "ৠ-6"
    VALUE_7 = "ৰ-7"
    VALUE_8 = "ਇ-8"
    VALUE_9 = "ਏ-9"


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
