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
    :cvar A40:
    :cvar A4:
    :cvar A4_A:
    :cvar A50:
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
    A00 = "a00ɶ"
    A0 = "a0-ɺ"
    A0_A = "a0Aɿ"
    A10 = "a10ʁ"
    A1 = "a1-ʔ"
    A1_A = "a1Aʨ"
    A20 = "a20ʻ"
    A2 = "a2-ʾ"
    A2_A = "a2Aˁ"
    A30 = "a30Ά"
    A40 = "a40Έ"
    A4 = "a4-Ή"
    A4_A = "a4AΊ"
    A50 = "a50Ό"
    A60 = "a60Ύ"
    A6 = "a6-Ύ"
    A6_A = "a6AΏ"
    A70 = "a70Α"
    A7 = "a7-Ι"
    A7_A = "a7AΡ"
    A80 = "a80Σ"
    A8 = "a8-Ω"
    A8_A = "a8Aί"
    A90 = "a90α"
    A9 = "a9-ο"
    A9_A = "a9Aώ"


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
