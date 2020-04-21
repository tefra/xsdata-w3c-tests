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
    :cvar A70:
    :cvar A80:
    :cvar A90:
    """
    A0 = "a0-Ọ"
    A00 = "a00Ạ"
    A0_A = "a0Aỹ"
    A1 = "a1-Ἂ"
    A10 = "a10ἀ"
    A1_A = "a1Aἕ"
    A2 = "a2-Ἒ"
    A20 = "a20Ἐ"
    A2_A = "a2AἝ"
    A3 = "a3-ἲ"
    A30 = "a30ἠ"
    A3_A = "a3Aὅ"
    A4 = "a4-Ὂ"
    A40 = "a40Ὀ"
    A4_A = "a4AὍ"
    A50 = "a50ὑ"
    A60 = "a60ὓ"
    A70 = "a70ὕ"
    A80 = "a80ὗ"
    A90 = "a90Ὑ"


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
