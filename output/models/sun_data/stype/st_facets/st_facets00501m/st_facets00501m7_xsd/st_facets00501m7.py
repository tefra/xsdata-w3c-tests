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
    :cvar A30:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
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
    A0 = "a0-এ"
    A00 = "a00এ"
    A0_A = "a0Aঐ"
    A1 = "a1-ঝ"
    A10 = "a10ও"
    A1_A = "a1Aন"
    A2 = "a2-ভ"
    A20 = "a20প"
    A2_A = "a2Aর"
    A30 = "a30ল"
    A4 = "a4-ষ"
    A40 = "a40শ"
    A4_A = "a4Aহ"
    A5 = "a5-ড়"
    A50 = "a50ড়"
    A5_A = "a5Aঢ়"
    A6 = "a6-ৠ"
    A60 = "a60য়"
    A6_A = "a6Aৡ"
    A7 = "a7-ৰ"
    A70 = "a70ৰ"
    A7_A = "a7Aৱ"
    A8 = "a8-ਇ"
    A80 = "a80ਅ"
    A8_A = "a8Aਊ"
    A9 = "a9-ਏ"
    A90 = "a90ਏ"
    A9_A = "a9Aਐ"


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
