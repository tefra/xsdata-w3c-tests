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
    :cvar A70:
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00ਓ"
    A0 = "a0-ਝ"
    A0_A = "a0Aਨ"
    A10 = "a10ਪ"
    A1 = "a1-ਭ"
    A1_A = "a1Aਰ"
    A20 = "a20ਲ"
    A2 = "a2-ਲ"
    A2_A = "a2Aਲ਼"
    A30 = "a30ਵ"
    A3 = "a3-ਵ"
    A3_A = "a3Aਸ਼"
    A40 = "a40ਸ"
    A4 = "a4-ਸ"
    A4_A = "a4Aਹ"
    A50 = "a50ਖ਼"
    A5 = "a5-ਗ਼"
    A5_A = "a5Aੜ"
    A60 = "a60ਫ਼"
    A70 = "a70ੲ"
    A7 = "a7-ੳ"
    A7_A = "a7Aੴ"
    A80 = "a80અ"
    A8 = "a8-ઈ"
    A8_A = "a8Aઋ"
    A90 = "a90ઍ"


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
