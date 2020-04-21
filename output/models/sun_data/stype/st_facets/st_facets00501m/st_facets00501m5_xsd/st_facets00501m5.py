from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A00:
    :cvar A0_A:
    :cvar A1:
    :cvar A10:
    :cvar A1_A:
    :cvar A2:
    :cvar A20:
    :cvar A2_A:
    :cvar A3:
    :cvar A30:
    :cvar A3_A:
    :cvar A40:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
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
    A0 = "a0-ӝ"
    A00 = "a00Ӑ"
    A0_A = "a0Aӫ"
    A1 = "a1-ӱ"
    A10 = "a10Ӯ"
    A1_A = "a1Aӵ"
    A2 = "a2-Ӹ"
    A20 = "a20Ӹ"
    A2_A = "a2Aӹ"
    A3 = "a3-Ճ"
    A30 = "a30Ա"
    A3_A = "a3AՖ"
    A40 = "a40ՙ"
    A5 = "a5-ճ"
    A50 = "a50ա"
    A5_A = "a5Aֆ"
    A6 = "a6-ם"
    A60 = "a60א"
    A6_A = "a6Aת"
    A7 = "a7-ױ"
    A70 = "a70װ"
    A7_A = "a7Aײ"
    A8 = "a8-ح"
    A80 = "a80ء"
    A8_A = "a8Aغ"
    A9 = "a9-م"
    A90 = "a90ف"
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
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
