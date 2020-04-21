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
    :cvar A60:
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
    A0 = "a0-ઐ"
    A00 = "a00એ"
    A0_A = "a0Aઑ"
    A1 = "a1-ઝ"
    A10 = "a10ઓ"
    A1_A = "a1Aન"
    A2 = "a2-ભ"
    A20 = "a20પ"
    A2_A = "a2Aર"
    A3 = "a3-લ"
    A30 = "a30લ"
    A3_A = "a3Aળ"
    A4 = "a4-ષ"
    A40 = "a40વ"
    A4_A = "a4Aહ"
    A50 = "a50ઽ"
    A60 = "a60ૠ"
    A7 = "a7-ଈ"
    A70 = "a70ଅ"
    A7_A = "a7Aଌ"
    A8 = "a8-ଏ"
    A80 = "a80ଏ"
    A8_A = "a8Aଐ"
    A9 = "a9-ଝ"
    A90 = "a90ଓ"
    A9_A = "a9Aନ"


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
