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
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
    :cvar A6:
    :cvar A60:
    :cvar A6_A:
    :cvar A70:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A9:
    :cvar A90:
    :cvar A9_A:
    """
    A0 = "a0-ష"
    A00 = "a00వ"
    A0_A = "a0Aహ"
    A1 = "a1-ౠ"
    A10 = "a10ౠ"
    A1_A = "a1Aౡ"
    A2 = "a2-ಈ"
    A20 = "a20ಅ"
    A2_A = "a2Aಌ"
    A3 = "a3-ಏ"
    A30 = "a30ಎ"
    A3_A = "a3Aಐ"
    A4 = "a4-ಝ"
    A40 = "a40ಒ"
    A4_A = "a4Aನ"
    A5 = "a5-ಮ"
    A50 = "a50ಪ"
    A5_A = "a5Aಳ"
    A6 = "a6-ಷ"
    A60 = "a60ವ"
    A6_A = "a6Aಹ"
    A70 = "a70ೞ"
    A8 = "a8-ೠ"
    A80 = "a80ೠ"
    A8_A = "a8Aೡ"
    A9 = "a9-ഈ"
    A90 = "a90അ"
    A9_A = "a9Aഌ"


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
