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
    A0 = "a0-ϓ"
    A00 = "a00ϐ"
    A0_A = "a0Aϖ"
    A1 = "a1-ϩ"
    A10 = "a10Ϣ"
    A1_A = "a1Aϱ"
    A2 = "a2-І"
    A20 = "a20Ё"
    A2_A = "a2AЌ"
    A3 = "a3-Ю"
    A30 = "a30Ў"
    A3_A = "a3Aя"
    A4 = "a4-і"
    A40 = "a40ё"
    A4_A = "a4Aќ"
    A5 = "a5-ѯ"
    A50 = "a50ў"
    A5_A = "a5Aҁ"
    A6 = "a6-ҧ"
    A60 = "a60Ґ"
    A6_A = "a6Aҿ"
    A7 = "a7-ӂ"
    A70 = "a70Ӂ"
    A7_A = "a7Aӄ"
    A8 = "a8-Ӈ"
    A80 = "a80Ӈ"
    A8_A = "a8Aӈ"
    A9 = "a9-Ӌ"
    A90 = "a90Ӌ"
    A9_A = "a9Aӌ"


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
