from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00_A:
    :cvar A0_M:
    :cvar A0_AZ:
    :cvar A10A:
    :cvar A1_D:
    :cvar A1_AH:
    :cvar A20J:
    :cvar A2_R:
    :cvar A2_AZ:
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
    A00_A = "a00A"
    A0_M = "a0-M"
    A0_AZ = "a0AZ"
    A10A = "a10a"
    A1_D = "a1-d"
    A1_AH = "a1Ah"
    A20J = "a20j"
    A2_R = "a2-r"
    A2_AZ = "a2Az"
    A30 = "a30À"
    A3 = "a3-Ë"
    A3_A = "a3AÖ"
    A40 = "a40Ø"
    A4 = "a4-Û"
    A4_A = "a4AÞ"
    A50 = "a50à"
    A5 = "a5-ë"
    A5_A = "a5Aö"
    A60 = "a60ø"
    A6 = "a6-û"
    A6_A = "a6Aÿ"
    A70 = "a70Ā"
    A7 = "a7-Ę"
    A7_A = "a7Aı"
    A80 = "a80Ĵ"
    A8 = "a8-Ĺ"
    A8_A = "a8Aľ"
    A90 = "a90Ł"
    A9 = "a9-ń"
    A9_A = "a9Aň"


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
