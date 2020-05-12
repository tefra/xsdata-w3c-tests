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
    :cvar A5:
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
    :cvar VALUE_5:
    :cvar VALUE_7:
    :cvar VALUE_8:
    """
    A0 = "ਨa0"
    A1 = "ਰa1"
    A2 = "ਲ਼a2"
    A3 = "ਸ਼a3"
    A4 = "ਹa4"
    A5 = "ੜa5"
    A7 = "ੴa7"
    A8 = "ઋa8"
    VALUE_0 = "ਝ-0"
    VALUE_00 = "ਓ00"
    VALUE_01 = "ਪ01"
    VALUE_02 = "ਲ02"
    VALUE_03 = "ਵ03"
    VALUE_04 = "ਸ04"
    VALUE_05 = "ਖ਼05"
    VALUE_06 = "ਫ਼06"
    VALUE_07 = "ੲ07"
    VALUE_08 = "અ08"
    VALUE_09 = "ઍ09"
    VALUE_1 = "ਭ-1"
    VALUE_2 = "ਲ-2"
    VALUE_3 = "ਵ-3"
    VALUE_4 = "ਸ-4"
    VALUE_5 = "ਗ਼-5"
    VALUE_7 = "ੳ-7"
    VALUE_8 = "ઈ-8"


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
