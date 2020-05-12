from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00_A:
    :cvar A0_AZ:
    :cvar A0_M:
    :cvar A10A:
    :cvar A1_AH:
    :cvar A1_D:
    :cvar A20J:
    :cvar A2_AZ:
    :cvar A2_R:
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
    A00_A = "a00A"
    A0_AZ = "a0AZ"
    A0_M = "a0-M"
    A10A = "a10a"
    A1_AH = "a1Ah"
    A1_D = "a1-d"
    A20J = "a20j"
    A2_AZ = "a2Az"
    A2_R = "a2-r"
    A3 = "a3-Ë"
    A30 = "a30À"
    A3_A = "a3AÖ"
    A4 = "a4-Û"
    A40 = "a40Ø"
    A4_A = "a4AÞ"
    A5 = "a5-ë"
    A50 = "a50à"
    A5_A = "a5Aö"
    A6 = "a6-û"
    A60 = "a60ø"
    A6_A = "a6Aÿ"
    A7 = "a7-Ę"
    A70 = "a70Ā"
    A7_A = "a7Aı"
    A8 = "a8-Ĺ"
    A80 = "a80Ĵ"
    A8_A = "a8Aľ"
    A9 = "a9-ń"
    A90 = "a90Ł"
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
