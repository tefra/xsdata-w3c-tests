from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A1:
    :cvar A10:
    :cvar A1_A:
    :cvar A2:
    :cvar A20:
    :cvar A2_A:
    :cvar A3:
    :cvar A30:
    :cvar A3_A:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A50:
    :cvar A6:
    :cvar A60:
    :cvar A6_A:
    :cvar A7:
    :cvar A70:
    :cvar A7_A:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A9:
    :cvar A90:
    :cvar A9_A:
    """
    A00 = "a00઼"
    A1 = "a1-ુ"
    A10 = "a10ા"
    A1_A = "a1Aૅ"
    A2 = "a2-ૈ"
    A20 = "a20ે"
    A2_A = "a2Aૉ"
    A3 = "a3-ૌ"
    A30 = "a30ો"
    A3_A = "a3A્"
    A4 = "a4-ଂ"
    A40 = "a40ଁ"
    A4_A = "a4Aଃ"
    A50 = "a50଼"
    A6 = "a6-ୀ"
    A60 = "a60ା"
    A6_A = "a6Aୃ"
    A7 = "a7-େ"
    A70 = "a70େ"
    A7_A = "a7Aୈ"
    A8 = "a8-ୌ"
    A80 = "a80ୋ"
    A8_A = "a8A୍"
    A9 = "a9-ୖ"
    A90 = "a90ୖ"
    A9_A = "a9Aୗ"


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
