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
    :cvar A30:
    :cvar A40:
    :cvar A50:
    :cvar A60:
    :cvar A70:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00ᄋ"
    A0 = "a0-ᄋ"
    A0_A = "a0Aᄌ"
    A10 = "a10ᄎ"
    A1 = "a1-ᄐ"
    A1_A = "a1Aᄒ"
    A20 = "a20ᄼ"
    A30 = "a30ᄾ"
    A40 = "a40ᅀ"
    A50 = "a50ᅌ"
    A60 = "a60ᅎ"
    A70 = "a70ᅐ"
    A80 = "a80ᅔ"
    A8 = "a8-ᅔ"
    A8_A = "a8Aᅕ"
    A90 = "a90ᅙ"


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
