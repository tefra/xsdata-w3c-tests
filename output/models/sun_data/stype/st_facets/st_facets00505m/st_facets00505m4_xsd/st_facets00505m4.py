from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A0:
    :cvar A00:
    :cvar A0_A:
    :cvar A10:
    :cvar A20:
    :cvar A30:
    :cvar A40:
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
    A0 = "a0-ৢ"
    A00 = "a00ৢ"
    A0_A = "a0Aৣ"
    A10 = "a10ਂ"
    A20 = "a20਼"
    A30 = "a30ਾ"
    A40 = "a40ਿ"
    A5 = "a5-ੁ"
    A50 = "a50ੀ"
    A5_A = "a5Aੂ"
    A6 = "a6-ੇ"
    A60 = "a60ੇ"
    A6_A = "a6Aੈ"
    A7 = "a7-ੌ"
    A70 = "a70ੋ"
    A7_A = "a7A੍"
    A8 = "a8-ੰ"
    A80 = "a80ੰ"
    A8_A = "a8Aੱ"
    A9 = "a9-ં"
    A90 = "a90ઁ"
    A9_A = "a9Aઃ"


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