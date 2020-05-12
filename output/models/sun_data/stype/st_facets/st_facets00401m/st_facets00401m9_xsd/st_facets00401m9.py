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
    :cvar VALUE_7:
    :cvar VALUE_8:
    :cvar VALUE_9:
    """
    A0 = "ઑa0"
    A1 = "નa1"
    A2 = "રa2"
    A3 = "ળa3"
    A4 = "હa4"
    A7 = "ଌa7"
    A8 = "ଐa8"
    A9 = "ନa9"
    VALUE_0 = "ઐ-0"
    VALUE_00 = "એ00"
    VALUE_01 = "ઓ01"
    VALUE_02 = "પ02"
    VALUE_03 = "લ03"
    VALUE_04 = "વ04"
    VALUE_05 = "ઽ05"
    VALUE_06 = "ૠ06"
    VALUE_07 = "ଅ07"
    VALUE_08 = "ଏ08"
    VALUE_09 = "ଓ09"
    VALUE_1 = "ઝ-1"
    VALUE_2 = "ભ-2"
    VALUE_3 = "લ-3"
    VALUE_4 = "ષ-4"
    VALUE_7 = "ଈ-7"
    VALUE_8 = "ଏ-8"
    VALUE_9 = "ଝ-9"


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
