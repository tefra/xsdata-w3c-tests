from enum import Enum
from dataclasses import dataclass, field
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
    :cvar VALUE_04:
    :cvar VALUE_4:
    :cvar A4:
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
    VALUE_00 = "ପ00"
    VALUE_0 = "ଭ-0"
    A0 = "ରa0"
    VALUE_01 = "ଲ01"
    VALUE_1 = "ଲ-1"
    A1 = "ଳa1"
    VALUE_02 = "ଶ02"
    VALUE_2 = "ଷ-2"
    A2 = "ହa2"
    VALUE_03 = "ଽ03"
    VALUE_04 = "ଡ଼04"
    VALUE_4 = "ଡ଼-4"
    A4 = "ଢ଼a4"
    VALUE_05 = "ୟ05"
    VALUE_5 = "ୠ-5"
    A5 = "ୡa5"
    VALUE_06 = "அ06"
    VALUE_6 = "இ-6"
    A6 = "ஊa6"
    VALUE_07 = "எ07"
    VALUE_7 = "ஏ-7"
    A7 = "ஐa7"
    VALUE_08 = "ஒ08"
    VALUE_8 = "ஓ-8"
    A8 = "கa8"
    VALUE_09 = "ங09"
    VALUE_9 = "ங-9"
    A9 = "சa9"


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
