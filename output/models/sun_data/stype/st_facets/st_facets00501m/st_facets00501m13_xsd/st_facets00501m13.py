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
    :cvar A50:
    :cvar A6:
    :cvar A60:
    :cvar A6_A:
    :cvar A7:
    :cvar A70:
    :cvar A7_A:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A90:
    """
    A0 = "a0-ഏ"
    A00 = "a00എ"
    A0_A = "a0Aഐ"
    A1 = "a1-ഝ"
    A10 = "a10ഒ"
    A1_A = "a1Aന"
    A2 = "a2-റ"
    A20 = "a20പ"
    A2_A = "a2Aഹ"
    A3 = "a3-ൠ"
    A30 = "a30ൠ"
    A3_A = "a3Aൡ"
    A4 = "a4-ท"
    A40 = "a40ก"
    A4_A = "a4Aฮ"
    A50 = "a50ะ"
    A6 = "a6-า"
    A60 = "a60า"
    A6_A = "a6Aำ"
    A7 = "a7-โ"
    A70 = "a70เ"
    A7_A = "a7Aๅ"
    A8 = "a8-ກ"
    A80 = "a80ກ"
    A8_A = "a8Aຂ"
    A90 = "a90ຄ"


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
