from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar VALUE_00:
    :cvar VALUE_01:
    :cvar VALUE_1:
    :cvar A1:
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
    :cvar VALUE_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    """
    VALUE_00 = "ະ00"
    VALUE_01 = "າ01"
    VALUE_1 = "າ-1"
    A1 = "ຳa1"
    VALUE_02 = "ຽ02"
    VALUE_03 = "ເ03"
    VALUE_3 = "ໂ-3"
    A3 = "ໄa3"
    VALUE_04 = "ཀ04"
    VALUE_4 = "གྷ-4"
    A4 = "ཇa4"
    VALUE_05 = "ཉ05"
    VALUE_5 = "ཙ-5"
    A5 = "ཀྵa5"
    VALUE_06 = "ᄀ06"
    VALUE_07 = "ᄂ07"
    VALUE_7 = "ᄂ-7"
    A7 = "ᄃa7"
    VALUE_08 = "ᄅ08"
    VALUE_8 = "ᄆ-8"
    A8 = "ᄇa8"
    VALUE_09 = "ᄉ09"


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
