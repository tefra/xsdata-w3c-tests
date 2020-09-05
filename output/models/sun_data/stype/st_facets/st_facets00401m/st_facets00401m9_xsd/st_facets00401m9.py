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
    :cvar VALUE_4:
    :cvar A4:
    :cvar VALUE_05:
    :cvar VALUE_06:
    :cvar VALUE_07:
    :cvar VALUE_7:
    :cvar A7:
    :cvar VALUE_08:
    :cvar VALUE_8:
    :cvar A8:
    :cvar VALUE_09:
    :cvar VALUE_9:
    :cvar A9:
    """
    VALUE_00 = "એ00"
    VALUE_0 = "ઐ-0"
    A0 = "ઑa0"
    VALUE_01 = "ઓ01"
    VALUE_1 = "ઝ-1"
    A1 = "નa1"
    VALUE_02 = "પ02"
    VALUE_2 = "ભ-2"
    A2 = "રa2"
    VALUE_03 = "લ03"
    VALUE_3 = "લ-3"
    A3 = "ળa3"
    VALUE_04 = "વ04"
    VALUE_4 = "ષ-4"
    A4 = "હa4"
    VALUE_05 = "ઽ05"
    VALUE_06 = "ૠ06"
    VALUE_07 = "ଅ07"
    VALUE_7 = "ଈ-7"
    A7 = "ଌa7"
    VALUE_08 = "ଏ08"
    VALUE_8 = "ଏ-8"
    A8 = "ଐa8"
    VALUE_09 = "ଓ09"
    VALUE_9 = "ଝ-9"
    A9 = "ନa9"


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
