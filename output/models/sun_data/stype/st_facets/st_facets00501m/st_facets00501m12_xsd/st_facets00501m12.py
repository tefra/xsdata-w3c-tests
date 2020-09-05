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
    :cvar A4:
    :cvar A4_A:
    :cvar A50:
    :cvar A5:
    :cvar A5_A:
    :cvar A60:
    :cvar A6:
    :cvar A6_A:
    :cvar A70:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A00 = "a00వ"
    A0 = "a0-ష"
    A0_A = "a0Aహ"
    A10 = "a10ౠ"
    A1 = "a1-ౠ"
    A1_A = "a1Aౡ"
    A20 = "a20ಅ"
    A2 = "a2-ಈ"
    A2_A = "a2Aಌ"
    A30 = "a30ಎ"
    A3 = "a3-ಏ"
    A3_A = "a3Aಐ"
    A40 = "a40ಒ"
    A4 = "a4-ಝ"
    A4_A = "a4Aನ"
    A50 = "a50ಪ"
    A5 = "a5-ಮ"
    A5_A = "a5Aಳ"
    A60 = "a60ವ"
    A6 = "a6-ಷ"
    A6_A = "a6Aಹ"
    A70 = "a70ೞ"
    A80 = "a80ೠ"
    A8 = "a8-ೠ"
    A8_A = "a8Aೡ"
    A90 = "a90അ"
    A9 = "a9-ഈ"
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
