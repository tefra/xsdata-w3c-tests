from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
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
    A00 = "a00ஜ"
    A1 = "a1-ஞ"
    A10 = "a10ஞ"
    A1_A = "a1Aட"
    A2 = "a2-ண"
    A20 = "a20ண"
    A2_A = "a2Aத"
    A3 = "a3-ன"
    A30 = "a30ந"
    A3_A = "a3Aப"
    A4 = "a4-ற"
    A40 = "a40ம"
    A4_A = "a4Aவ"
    A5 = "a5-ஸ"
    A50 = "a50ஷ"
    A5_A = "a5Aஹ"
    A6 = "a6-ఈ"
    A60 = "a60అ"
    A6_A = "a6Aఌ"
    A7 = "a7-ఏ"
    A70 = "a70ఎ"
    A7_A = "a7Aఐ"
    A8 = "a8-ఝ"
    A80 = "a80ఒ"
    A8_A = "a8Aన"
    A9 = "a9-మ"
    A90 = "a90ప"
    A9_A = "a9Aళ"


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
