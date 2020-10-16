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
    :cvar VALUE_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    """
    VALUE_00 = "ਓ00"
    VALUE_0 = "ਝ-0"
    A0 = "ਨa0"
    VALUE_01 = "ਪ01"
    VALUE_1 = "ਭ-1"
    A1 = "ਰa1"
    VALUE_02 = "ਲ02"
    VALUE_2 = "ਲ-2"
    A2 = "ਲ਼a2"
    VALUE_03 = "ਵ03"
    VALUE_3 = "ਵ-3"
    A3 = "ਸ਼a3"
    VALUE_04 = "ਸ04"
    VALUE_4 = "ਸ-4"
    A4 = "ਹa4"
    VALUE_05 = "ਖ਼05"
    VALUE_5 = "ਗ਼-5"
    A5 = "ੜa5"
    VALUE_06 = "ਫ਼06"
    VALUE_07 = "ੲ07"
    VALUE_7 = "ੳ-7"
    A7 = "ੴa7"
    VALUE_08 = "અ08"
    VALUE_8 = "ઈ-8"
    A8 = "ઋa8"
    VALUE_09 = "ઍ09"


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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
