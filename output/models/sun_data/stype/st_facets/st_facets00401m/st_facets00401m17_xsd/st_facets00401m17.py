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
    :cvar VALUE_02:
    :cvar VALUE_03:
    :cvar VALUE_04:
    :cvar VALUE_MINUS_5:
    :cvar VALUE_05:
    :cvar A5:
    :cvar VALUE_MINUS_6:
    :cvar VALUE_06:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_08:
    :cvar VALUE_09:
    """
    VALUE_00 = "ᅟ00"
    VALUE_MINUS_0 = "ᅠ-0"
    A0 = "ᅡa0"
    VALUE_01 = "ᅣ01"
    VALUE_02 = "ᅥ02"
    VALUE_03 = "ᅧ03"
    VALUE_04 = "ᅩ04"
    VALUE_MINUS_5 = "ᅭ-5"
    VALUE_05 = "ᅭ05"
    A5 = "ᅮa5"
    VALUE_MINUS_6 = "ᅲ-6"
    VALUE_06 = "ᅲ06"
    A6 = "ᅳa6"
    VALUE_07 = "ᅵ07"
    VALUE_08 = "ᆞ08"
    VALUE_09 = "ᆨ09"


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
