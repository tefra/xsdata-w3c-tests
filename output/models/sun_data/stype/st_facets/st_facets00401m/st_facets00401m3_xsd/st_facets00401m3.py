from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_MINUS_0:
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
    :cvar VALUE_05:
    :cvar VALUE_MINUS_6:
    :cvar VALUE_06:
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
    VALUE_00 = "ɶ00"
    VALUE_MINUS_0 = "ɺ-0"
    A0 = "ɿa0"
    VALUE_01 = "ʁ01"
    VALUE_MINUS_1 = "ʔ-1"
    A1 = "ʨa1"
    VALUE_02 = "ʻ02"
    VALUE_MINUS_2 = "ʾ-2"
    A2 = "ˁa2"
    VALUE_03 = "Ά03"
    VALUE_04 = "Έ04"
    VALUE_MINUS_4 = "Ή-4"
    A4 = "Ίa4"
    VALUE_05 = "Ό05"
    VALUE_MINUS_6 = "Ύ-6"
    VALUE_06 = "Ύ06"
    A6 = "Ώa6"
    VALUE_07 = "Α07"
    VALUE_MINUS_7 = "Ι-7"
    A7 = "Ρa7"
    VALUE_08 = "Σ08"
    VALUE_MINUS_8 = "Ω-8"
    A8 = "ίa8"
    VALUE_09 = "α09"
    VALUE_MINUS_9 = "ο-9"
    A9 = "ώa9"


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
