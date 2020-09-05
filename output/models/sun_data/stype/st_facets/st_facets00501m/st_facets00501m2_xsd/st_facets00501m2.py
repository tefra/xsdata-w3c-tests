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
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A00 = "a00Ŋ"
    A0 = "a0-Ť"
    A0_A = "a0Až"
    A10 = "a10ƀ"
    A1 = "a1-Ɗ"
    A1_A = "a1AƔ"
    A20 = "a20Ɩ"
    A2 = "a2-Ɲ"
    A2_A = "a2Aƥ"
    A30 = "a30Ƨ"
    A3 = "a3-ƨ"
    A3_A = "a3AƩ"
    A40 = "a40ƫ"
    A4 = "a4-ƴ"
    A4_A = "a4Aƽ"
    A50 = "a50ǀ"
    A5 = "a5-ǁ"
    A5_A = "a5Aǃ"
    A60 = "a60Ǎ"
    A6 = "a6-Ǟ"
    A6_A = "a6Aǯ"
    A70 = "a70Ǵ"
    A7 = "a7-Ǵ"
    A7_A = "a7Aǵ"
    A80 = "a80Ǻ"
    A8 = "a8-Ȉ"
    A8_A = "a8Aȗ"
    A90 = "a90ɐ"
    A9 = "a9-ɢ"
    A9_A = "a9Aɴ"


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
