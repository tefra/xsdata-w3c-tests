from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A10:
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
    A00 = "a00༹"
    A10 = "a10༾"
    A20 = "a20༿"
    A3 = "a3-ེ"
    A30 = "a30ཱ"
    A3_A = "a3A྄"
    A4 = "a4-྆"
    A40 = "a40྆"
    A4_A = "a4A྇"
    A5 = "a5-ྒ"
    A50 = "a50ྐ"
    A5_A = "a5Aྕ"
    A60 = "a60ྗ"
    A7 = "a7-ྣ"
    A70 = "a70ྙ"
    A7_A = "a7Aྭ"
    A8 = "a8-ྴ"
    A80 = "a80ྱ"
    A8_A = "a8Aྷ"
    A90 = "a90ྐྵ"


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
