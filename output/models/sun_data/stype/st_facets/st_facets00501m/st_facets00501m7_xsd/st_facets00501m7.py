from enum import Enum
from dataclasses import dataclass, field
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
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A00 = "a00এ"
    A0 = "a0-এ"
    A0_A = "a0Aঐ"
    A10 = "a10ও"
    A1 = "a1-ঝ"
    A1_A = "a1Aন"
    A20 = "a20প"
    A2 = "a2-ভ"
    A2_A = "a2Aর"
    A30 = "a30ল"
    A40 = "a40শ"
    A4 = "a4-ষ"
    A4_A = "a4Aহ"
    A50 = "a50ড়"
    A5 = "a5-ড়"
    A5_A = "a5Aঢ়"
    A60 = "a60য়"
    A6 = "a6-ৠ"
    A6_A = "a6Aৡ"
    A70 = "a70ৰ"
    A7 = "a7-ৰ"
    A7_A = "a7Aৱ"
    A80 = "a80ਅ"
    A8 = "a8-ਇ"
    A8_A = "a8Aਊ"
    A90 = "a90ਏ"
    A9 = "a9-ਏ"
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
