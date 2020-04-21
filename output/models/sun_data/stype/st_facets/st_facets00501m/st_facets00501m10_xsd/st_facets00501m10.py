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
    A0 = "a0-ଭ"
    A00 = "a00ପ"
    A0_A = "a0Aର"
    A1 = "a1-ଲ"
    A10 = "a10ଲ"
    A1_A = "a1Aଳ"
    A2 = "a2-ଷ"
    A20 = "a20ଶ"
    A2_A = "a2Aହ"
    A30 = "a30ଽ"
    A4 = "a4-ଡ଼"
    A40 = "a40ଡ଼"
    A4_A = "a4Aଢ଼"
    A5 = "a5-ୠ"
    A50 = "a50ୟ"
    A5_A = "a5Aୡ"
    A6 = "a6-இ"
    A60 = "a60அ"
    A6_A = "a6Aஊ"
    A7 = "a7-ஏ"
    A70 = "a70எ"
    A7_A = "a7Aஐ"
    A8 = "a8-ஓ"
    A80 = "a80ஒ"
    A8_A = "a8Aக"
    A9 = "a9-ங"
    A90 = "a90ங"
    A9_A = "a9Aச"


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
