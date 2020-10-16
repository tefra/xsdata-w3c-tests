from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_0:
    :cvar A0:
    :cvar VALUE_01:
    :cvar VALUE_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_2:
    :cvar A2:
    :cvar VALUE_03:
    :cvar VALUE_3:
    :cvar A3:
    :cvar VALUE_04:
    :cvar VALUE_05:
    :cvar VALUE_5:
    :cvar A5:
    :cvar VALUE_06:
    :cvar VALUE_6:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_9:
    :cvar A9:
    """
    VALUE_00 = "ٱ00"
    VALUE_0 = "ڔ-0"
    A0 = "ڷa0"
    VALUE_01 = "ں01"
    VALUE_1 = "ڼ-1"
    A1 = "ھa1"
    VALUE_02 = "ۀ02"
    VALUE_2 = "ۇ-2"
    A2 = "ێa2"
    VALUE_03 = "ې03"
    VALUE_3 = "ۑ-3"
    A3 = "ۓa3"
    VALUE_04 = "ە04"
    VALUE_05 = "ۥ05"
    VALUE_5 = "ۥ-5"
    A5 = "ۦa5"
    VALUE_06 = "अ06"
    VALUE_6 = "ट-6"
    A6 = "हa6"
    VALUE_07 = "ऽ07"
    VALUE_08 = "क़08"
    VALUE_8 = "ड़-8"
    A8 = "ॡa8"
    VALUE_09 = "অ09"
    VALUE_9 = "ঈ-9"
    A9 = "ঌa9"


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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
