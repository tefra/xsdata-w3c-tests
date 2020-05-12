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
    :cvar VALUE_02:
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
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_9:
    :cvar A9:
    """
    VALUE_00 = "ງ00"
    VALUE_0 = "ງ-0"
    A0 = "ຈa0"
    VALUE_01 = "ຊ01"
    VALUE_02 = "ຍ02"
    VALUE_03 = "ດ03"
    VALUE_3 = "ຕ-3"
    A3 = "ທa3"
    VALUE_04 = "ນ04"
    VALUE_4 = "ຜ-4"
    A4 = "ຟa4"
    VALUE_05 = "ມ05"
    VALUE_5 = "ຢ-5"
    A5 = "ຣa5"
    VALUE_06 = "ລ06"
    VALUE_07 = "ວ07"
    VALUE_08 = "ສ08"
    VALUE_8 = "ສ-8"
    A8 = "ຫa8"
    VALUE_09 = "ອ09"
    VALUE_9 = "ອ-9"
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
