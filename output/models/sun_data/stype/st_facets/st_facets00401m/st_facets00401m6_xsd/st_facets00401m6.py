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
    :cvar A5:
    :cvar A6:
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
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ڷa0"
    A1 = "ھa1"
    A2 = "ێa2"
    A3 = "ۓa3"
    A5 = "ۦa5"
    A6 = "हa6"
    A8 = "ॡa8"
    A9 = "ঌa9"
    VALUE_0 = "ڔ-0"
    VALUE_00 = "ٱ00"
    VALUE_01 = "ں01"
    VALUE_02 = "ۀ02"
    VALUE_03 = "ې03"
    VALUE_04 = "ە04"
    VALUE_05 = "ۥ05"
    VALUE_06 = "अ06"
    VALUE_07 = "ऽ07"
    VALUE_08 = "क़08"
    VALUE_09 = "অ09"
    VALUE_1 = "ڼ-1"
    VALUE_2 = "ۇ-2"
    VALUE_3 = "ۑ-3"
    VALUE_5 = "ۥ-5"
    VALUE_6 = "ट-6"
    VALUE_8 = "ड़-8"
    VALUE_9 = "ঈ-9"


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
