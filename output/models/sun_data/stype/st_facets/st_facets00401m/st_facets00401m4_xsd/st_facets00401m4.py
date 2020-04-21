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
    :cvar VALUE_MINUS_1:
    :cvar A1:
    :cvar VALUE_02:
    :cvar VALUE_MINUS_2:
    :cvar A2:
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
    :cvar VALUE_MINUS_6:
    :cvar A6:
    :cvar VALUE_07:
    :cvar VALUE_MINUS_7:
    :cvar A7:
    :cvar VALUE_MINUS_8:
    :cvar VALUE_08:
    :cvar A8:
    :cvar VALUE_MINUS_9:
    :cvar VALUE_09:
    :cvar A9:
    """
    VALUE_00 = "ϐ00"
    VALUE_MINUS_0 = "ϓ-0"
    A0 = "ϖa0"
    VALUE_01 = "Ϣ01"
    VALUE_MINUS_1 = "ϩ-1"
    A1 = "ϱa1"
    VALUE_02 = "Ё02"
    VALUE_MINUS_2 = "І-2"
    A2 = "Ќa2"
    VALUE_03 = "Ў03"
    VALUE_MINUS_3 = "Ю-3"
    A3 = "яa3"
    VALUE_04 = "ё04"
    VALUE_MINUS_4 = "і-4"
    A4 = "ќa4"
    VALUE_05 = "ў05"
    VALUE_MINUS_5 = "ѯ-5"
    A5 = "ҁa5"
    VALUE_06 = "Ґ06"
    VALUE_MINUS_6 = "ҧ-6"
    A6 = "ҿa6"
    VALUE_07 = "Ӂ07"
    VALUE_MINUS_7 = "ӂ-7"
    A7 = "ӄa7"
    VALUE_MINUS_8 = "Ӈ-8"
    VALUE_08 = "Ӈ08"
    A8 = "ӈa8"
    VALUE_MINUS_9 = "Ӌ-9"
    VALUE_09 = "Ӌ09"
    A9 = "ӌa9"


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
