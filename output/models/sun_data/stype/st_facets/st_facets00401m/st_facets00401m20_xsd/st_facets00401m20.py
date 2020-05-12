from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A2:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A6:
    :cvar A7:
    :cvar A8:
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
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    """
    A2 = "ώa2"
    A3 = "ᾱa3"
    A4 = "Άa4"
    A5 = "Ήa5"
    A6 = "ῑa6"
    A7 = "Ίa7"
    A8 = "ῡa8"
    VALUE_00 = "Ὓ00"
    VALUE_01 = "Ὕ01"
    VALUE_02 = "Ὗ02"
    VALUE_03 = "ᾰ03"
    VALUE_04 = "Ᾰ04"
    VALUE_05 = "Ὲ05"
    VALUE_06 = "ῐ06"
    VALUE_07 = "Ῐ07"
    VALUE_08 = "ῠ08"
    VALUE_09 = "ῥ09"
    VALUE_2 = "Ὦ-2"
    VALUE_3 = "ᾰ-3"
    VALUE_4 = "Ᾱ-4"
    VALUE_5 = "Έ-5"
    VALUE_6 = "ῐ-6"
    VALUE_7 = "Ῑ-7"
    VALUE_8 = "ῠ-8"


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
