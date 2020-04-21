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
    :cvar A30:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A50:
    :cvar A60:
    :cvar A70:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00ᆫ"
    A1 = "a1-ᆮ"
    A10 = "a10ᆮ"
    A1_A = "a1Aᆯ"
    A2 = "a2-ᆷ"
    A20 = "a20ᆷ"
    A2_A = "a2Aᆸ"
    A30 = "a30ᆺ"
    A4 = "a4-ᆿ"
    A40 = "a40ᆼ"
    A4_A = "a4Aᇂ"
    A50 = "a50ᇫ"
    A60 = "a60ᇰ"
    A70 = "a70ᇹ"
    A8 = "a8-Ṋ"
    A80 = "a80Ḁ"
    A8_A = "a8Aẕ"
    A90 = "a90ẛ"


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
