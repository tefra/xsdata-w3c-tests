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
    :cvar A60:
    :cvar A7:
    :cvar A70:
    :cvar A7_A:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A90:
    """
    A0 = "a0-ਝ"
    A00 = "a00ਓ"
    A0_A = "a0Aਨ"
    A1 = "a1-ਭ"
    A10 = "a10ਪ"
    A1_A = "a1Aਰ"
    A2 = "a2-ਲ"
    A20 = "a20ਲ"
    A2_A = "a2Aਲ਼"
    A3 = "a3-ਵ"
    A30 = "a30ਵ"
    A3_A = "a3Aਸ਼"
    A4 = "a4-ਸ"
    A40 = "a40ਸ"
    A4_A = "a4Aਹ"
    A5 = "a5-ਗ਼"
    A50 = "a50ਖ਼"
    A5_A = "a5Aੜ"
    A60 = "a60ਫ਼"
    A7 = "a7-ੳ"
    A70 = "a70ੲ"
    A7_A = "a7Aੴ"
    A8 = "a8-ઈ"
    A80 = "a80અ"
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
