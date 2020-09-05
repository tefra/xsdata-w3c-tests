from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A10:
    :cvar A1:
    :cvar A1_A:
    :cvar A20:
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
    :cvar A70:
    :cvar A7:
    :cvar A7_A:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    """
    A00 = "a00ະ"
    A10 = "a10າ"
    A1 = "a1-າ"
    A1_A = "a1Aຳ"
    A20 = "a20ຽ"
    A30 = "a30ເ"
    A3 = "a3-ໂ"
    A3_A = "a3Aໄ"
    A40 = "a40ཀ"
    A4 = "a4-གྷ"
    A4_A = "a4Aཇ"
    A50 = "a50ཉ"
    A5 = "a5-ཙ"
    A5_A = "a5Aཀྵ"
    A60 = "a60ᄀ"
    A70 = "a70ᄂ"
    A7 = "a7-ᄂ"
    A7_A = "a7Aᄃ"
    A80 = "a80ᄅ"
    A8 = "a8-ᄆ"
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
