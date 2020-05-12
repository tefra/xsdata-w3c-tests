from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A1:
    :cvar A3:
    :cvar A4:
    :cvar A5:
    :cvar A7:
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
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_7:
    :cvar VALUE_8:
    """
    A1 = "ຳa1"
    A3 = "ໄa3"
    A4 = "ཇa4"
    A5 = "ཀྵa5"
    A7 = "ᄃa7"
    A8 = "ᄇa8"
    VALUE_00 = "ະ00"
    VALUE_01 = "າ01"
    VALUE_02 = "ຽ02"
    VALUE_03 = "ເ03"
    VALUE_04 = "ཀ04"
    VALUE_05 = "ཉ05"
    VALUE_06 = "ᄀ06"
    VALUE_07 = "ᄂ07"
    VALUE_08 = "ᄅ08"
    VALUE_09 = "ᄉ09"
    VALUE_1 = "າ-1"
    VALUE_3 = "ໂ-3"
    VALUE_4 = "གྷ-4"
    VALUE_5 = "ཙ-5"
    VALUE_7 = "ᄂ-7"
    VALUE_8 = "ᄆ-8"


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
