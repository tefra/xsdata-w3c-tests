from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A1:
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
    :cvar VALUE_8:
    """
    A0 = "ᄌa0"
    A1 = "ᄒa1"
    A8 = "ᅕa8"
    VALUE_0 = "ᄋ-0"
    VALUE_00 = "ᄋ00"
    VALUE_01 = "ᄎ01"
    VALUE_02 = "ᄼ02"
    VALUE_03 = "ᄾ03"
    VALUE_04 = "ᅀ04"
    VALUE_05 = "ᅌ05"
    VALUE_06 = "ᅎ06"
    VALUE_07 = "ᅐ07"
    VALUE_08 = "ᅔ08"
    VALUE_09 = "ᅙ09"
    VALUE_1 = "ᄐ-1"
    VALUE_8 = "ᅔ-8"


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
