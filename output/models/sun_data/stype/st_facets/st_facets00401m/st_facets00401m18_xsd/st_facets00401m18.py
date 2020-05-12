from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A1:
    :cvar A2:
    :cvar A4:
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
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_4:
    :cvar VALUE_8:
    """
    A1 = "ᆯa1"
    A2 = "ᆸa2"
    A4 = "ᇂa4"
    A8 = "ẕa8"
    VALUE_00 = "ᆫ00"
    VALUE_01 = "ᆮ01"
    VALUE_02 = "ᆷ02"
    VALUE_03 = "ᆺ03"
    VALUE_04 = "ᆼ04"
    VALUE_05 = "ᇫ05"
    VALUE_06 = "ᇰ06"
    VALUE_07 = "ᇹ07"
    VALUE_08 = "Ḁ08"
    VALUE_09 = "ẛ09"
    VALUE_1 = "ᆮ-1"
    VALUE_2 = "ᆷ-2"
    VALUE_4 = "ᆿ-4"
    VALUE_8 = "Ṋ-8"


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
