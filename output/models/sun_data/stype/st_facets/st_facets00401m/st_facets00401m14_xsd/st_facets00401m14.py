from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A8:
    :cvar A9:
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
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ຈa0"
    A3 = "ທa3"
    A4 = "ຟa4"
    A5 = "ຣa5"
    A8 = "ຫa8"
    A9 = "ຮa9"
    VALUE_0 = "ງ-0"
    VALUE_00 = "ງ00"
    VALUE_01 = "ຊ01"
    VALUE_02 = "ຍ02"
    VALUE_03 = "ດ03"
    VALUE_04 = "ນ04"
    VALUE_05 = "ມ05"
    VALUE_06 = "ລ06"
    VALUE_07 = "ວ07"
    VALUE_08 = "ສ08"
    VALUE_09 = "ອ09"
    VALUE_3 = "ຕ-3"
    VALUE_4 = "ຜ-4"
    VALUE_5 = "ຢ-5"
    VALUE_8 = "ສ-8"
    VALUE_9 = "ອ-9"


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
