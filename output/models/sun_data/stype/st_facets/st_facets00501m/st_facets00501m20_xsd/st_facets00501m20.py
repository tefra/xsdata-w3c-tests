from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A10:
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
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00Ὓ"
    A10 = "a10Ὕ"
    A20 = "a20Ὗ"
    A2 = "a2-Ὦ"
    A2_A = "a2Aώ"
    A30 = "a30ᾰ"
    A3 = "a3-ᾰ"
    A3_A = "a3Aᾱ"
    A40 = "a40Ᾰ"
    A4 = "a4-Ᾱ"
    A4_A = "a4AΆ"
    A50 = "a50Ὲ"
    A5 = "a5-Έ"
    A5_A = "a5AΉ"
    A60 = "a60ῐ"
    A6 = "a6-ῐ"
    A6_A = "a6Aῑ"
    A70 = "a70Ῐ"
    A7 = "a7-Ῑ"
    A7_A = "a7AΊ"
    A80 = "a80ῠ"
    A8 = "a8-ῠ"
    A8_A = "a8Aῡ"
    A90 = "a90ῥ"


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
