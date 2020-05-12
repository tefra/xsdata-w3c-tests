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
    :cvar A4:
    :cvar A5:
    :cvar A6:
    :cvar A7:
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
    :cvar VALUE_4:
    :cvar VALUE_5:
    :cvar VALUE_6:
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ϖa0"
    A1 = "ϱa1"
    A2 = "Ќa2"
    A3 = "яa3"
    A4 = "ќa4"
    A5 = "ҁa5"
    A6 = "ҿa6"
    A7 = "ӄa7"
    A8 = "ӈa8"
    A9 = "ӌa9"
    VALUE_0 = "ϓ-0"
    VALUE_00 = "ϐ00"
    VALUE_01 = "Ϣ01"
    VALUE_02 = "Ё02"
    VALUE_03 = "Ў03"
    VALUE_04 = "ё04"
    VALUE_05 = "ў05"
    VALUE_06 = "Ґ06"
    VALUE_07 = "Ӂ07"
    VALUE_08 = "Ӈ08"
    VALUE_09 = "Ӌ09"
    VALUE_1 = "ϩ-1"
    VALUE_2 = "І-2"
    VALUE_3 = "Ю-3"
    VALUE_4 = "і-4"
    VALUE_5 = "ѯ-5"
    VALUE_6 = "ҧ-6"
    VALUE_7 = "ӂ-7"
    VALUE_8 = "Ӈ-8"
    VALUE_9 = "Ӌ-9"


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
