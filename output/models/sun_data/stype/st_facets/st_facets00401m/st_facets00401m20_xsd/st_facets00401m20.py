from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_MINUS_2:
    :cvar A2:
    :cvar VALUE_MINUS_3:
    :cvar VALUE_03:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_MINUS_5:
    :cvar A5:
    :cvar VALUE_MINUS_6:
    :cvar VALUE_06:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_MINUS_7:
    :cvar A7:
    :cvar VALUE_MINUS_8:
    :cvar VALUE_08:
    :cvar A8:
    :cvar VALUE_09:
    """
    VALUE_00 = "Ὓ00"
    VALUE_01 = "Ὕ01"
    VALUE_02 = "Ὗ02"
    VALUE_MINUS_2 = "Ὦ-2"
    A2 = "ώa2"
    VALUE_MINUS_3 = "ᾰ-3"
    VALUE_03 = "ᾰ03"
    A3 = "ᾱa3"
    VALUE_04 = "Ᾰ04"
    VALUE_MINUS_4 = "Ᾱ-4"
    A4 = "Άa4"
    VALUE_05 = "Ὲ05"
    VALUE_MINUS_5 = "Έ-5"
    A5 = "Ήa5"
    VALUE_MINUS_6 = "ῐ-6"
    VALUE_06 = "ῐ06"
    A6 = "ῑa6"
    VALUE_07 = "Ῐ07"
    VALUE_MINUS_7 = "Ῑ-7"
    A7 = "Ίa7"
    VALUE_MINUS_8 = "ῠ-8"
    VALUE_08 = "ῠ08"
    A8 = "ῡa8"
    VALUE_09 = "ῥ09"


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