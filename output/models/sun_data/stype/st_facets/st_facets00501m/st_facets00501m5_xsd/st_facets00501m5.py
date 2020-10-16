from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A0:
    :cvar A0_A:
    :cvar A10:
    :cvar A1:
    :cvar A1_A:
    :cvar A20:
    :cvar A2:
    :cvar A2_A:
    :cvar A30:
    :cvar A3:
    :cvar A3_A:
    :cvar A40:
    :cvar A50:
    :cvar A5:
    :cvar A5_A:
    :cvar A60:
    :cvar A6:
    :cvar A6_A:
    :cvar A70:
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A00 = "a00Ӑ"
    A0 = "a0-ӝ"
    A0_A = "a0Aӫ"
    A10 = "a10Ӯ"
    A1 = "a1-ӱ"
    A1_A = "a1Aӵ"
    A20 = "a20Ӹ"
    A2 = "a2-Ӹ"
    A2_A = "a2Aӹ"
    A30 = "a30Ա"
    A3 = "a3-Ճ"
    A3_A = "a3AՖ"
    A40 = "a40ՙ"
    A50 = "a50ա"
    A5 = "a5-ճ"
    A5_A = "a5Aֆ"
    A60 = "a60א"
    A6 = "a6-ם"
    A6_A = "a6Aת"
    A70 = "a70װ"
    A7 = "a7-ױ"
    A7_A = "a7Aײ"
    A80 = "a80ء"
    A8 = "a8-ح"
    A8_A = "a8Aغ"
    A90 = "a90ف"
    A9 = "a9-م"
    A9_A = "a9Aي"


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
