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
    """
    A0 = "ỹa0"
    A1 = "ἕa1"
    A2 = "Ἕa2"
    A3 = "ὅa3"
    A4 = "Ὅa4"
    VALUE_0 = "Ọ-0"
    VALUE_00 = "Ạ00"
    VALUE_01 = "ἀ01"
    VALUE_02 = "Ἐ02"
    VALUE_03 = "ἠ03"
    VALUE_04 = "Ὀ04"
    VALUE_05 = "ὑ05"
    VALUE_06 = "ὓ06"
    VALUE_07 = "ὕ07"
    VALUE_08 = "ὗ08"
    VALUE_09 = "Ὑ09"
    VALUE_1 = "Ἂ-1"
    VALUE_2 = "Ἒ-2"
    VALUE_3 = "ἲ-3"
    VALUE_4 = "Ὂ-4"


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
