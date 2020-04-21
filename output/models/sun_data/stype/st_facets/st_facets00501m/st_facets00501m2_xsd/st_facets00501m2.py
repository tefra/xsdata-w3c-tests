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
    A0 = "a0-Ť"
    A00 = "a00Ŋ"
    A0_A = "a0Až"
    A1 = "a1-Ɗ"
    A10 = "a10ƀ"
    A1_A = "a1AƔ"
    A2 = "a2-Ɲ"
    A20 = "a20Ɩ"
    A2_A = "a2Aƥ"
    A3 = "a3-ƨ"
    A30 = "a30Ƨ"
    A3_A = "a3AƩ"
    A4 = "a4-ƴ"
    A40 = "a40ƫ"
    A4_A = "a4Aƽ"
    A5 = "a5-ǁ"
    A50 = "a50ǀ"
    A5_A = "a5Aǃ"
    A6 = "a6-Ǟ"
    A60 = "a60Ǎ"
    A6_A = "a6Aǯ"
    A7 = "a7-Ǵ"
    A70 = "a70Ǵ"
    A7_A = "a7Aǵ"
    A8 = "a8-Ȉ"
    A80 = "a80Ǻ"
    A8_A = "a8Aȗ"
    A9 = "a9-ɢ"
    A90 = "a90ɐ"
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
