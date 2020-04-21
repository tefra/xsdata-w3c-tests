from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_MINUS_0:
    :cvar VALUE_00:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_02:
    :cvar VALUE_03:
    :cvar VALUE_MINUS_3:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_MINUS_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_MINUS_8:
    :cvar VALUE_08:
    :cvar A8:
    :cvar VALUE_MINUS_9:
    :cvar VALUE_09:
    :cvar A9:
    """
    VALUE_MINUS_0 = "ງ-0"
    VALUE_00 = "ງ00"
    A0 = "ຈa0"
    VALUE_01 = "ຊ01"
    VALUE_02 = "ຍ02"
    VALUE_03 = "ດ03"
    VALUE_MINUS_3 = "ຕ-3"
    A3 = "ທa3"
    VALUE_04 = "ນ04"
    VALUE_MINUS_4 = "ຜ-4"
    A4 = "ຟa4"
    VALUE_05 = "ມ05"
    VALUE_MINUS_5 = "ຢ-5"
    A5 = "ຣa5"
    VALUE_06 = "ລ06"
    VALUE_07 = "ວ07"
    VALUE_MINUS_8 = "ສ-8"
    VALUE_08 = "ສ08"
    A8 = "ຫa8"
    VALUE_MINUS_9 = "ອ-9"
    VALUE_09 = "ອ09"
    A9 = "ຮa9"


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
