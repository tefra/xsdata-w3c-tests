from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_MINUS_1:
    :cvar VALUE_01:
    :cvar A1:
    :cvar VALUE_MINUS_2:
    :cvar VALUE_02:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_08:
    :cvar VALUE_MINUS_8:
    :cvar A8:
    :cvar VALUE_09:
    """
    VALUE_00 = "ᆫ00"
    VALUE_MINUS_1 = "ᆮ-1"
    VALUE_01 = "ᆮ01"
    A1 = "ᆯa1"
    VALUE_MINUS_2 = "ᆷ-2"
    VALUE_02 = "ᆷ02"
    A2 = "ᆸa2"
    VALUE_03 = "ᆺ03"
    VALUE_04 = "ᆼ04"
    VALUE_MINUS_4 = "ᆿ-4"
    A4 = "ᇂa4"
    VALUE_05 = "ᇫ05"
    VALUE_06 = "ᇰ06"
    VALUE_07 = "ᇹ07"
    VALUE_08 = "Ḁ08"
    VALUE_MINUS_8 = "Ṋ-8"
    A8 = "ẕa8"
    VALUE_09 = "ẛ09"


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