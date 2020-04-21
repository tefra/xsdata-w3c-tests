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
    :cvar A20:
    :cvar A3:
    :cvar A30:
    :cvar A3_A:
    :cvar A4:
    :cvar A40:
    :cvar A4_A:
    :cvar A5:
    :cvar A50:
    :cvar A5_A:
    :cvar A60:
    :cvar A7:
    :cvar A70:
    :cvar A7_A:
    :cvar A8:
    :cvar A80:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00ະ"
    A1 = "a1-າ"
    A10 = "a10າ"
    A1_A = "a1Aຳ"
    A20 = "a20ຽ"
    A3 = "a3-ໂ"
    A30 = "a30ເ"
    A3_A = "a3Aໄ"
    A4 = "a4-གྷ"
    A40 = "a40ཀ"
    A4_A = "a4Aཇ"
    A5 = "a5-ཙ"
    A50 = "a50ཉ"
    A5_A = "a5Aཀྵ"
    A60 = "a60ᄀ"
    A7 = "a7-ᄂ"
    A70 = "a70ᄂ"
    A7_A = "a7Aᄃ"
    A8 = "a8-ᄆ"
    A80 = "a80ᄅ"
    A8_A = "a8Aᄇ"
    A90 = "a90ᄉ"


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
