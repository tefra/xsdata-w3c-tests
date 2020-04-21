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
    :cvar A70:
    :cvar A80:
    :cvar A90:
    """
    A0 = "a0-ᅠ"
    A00 = "a00ᅟ"
    A0_A = "a0Aᅡ"
    A10 = "a10ᅣ"
    A20 = "a20ᅥ"
    A30 = "a30ᅧ"
    A40 = "a40ᅩ"
    A5 = "a5-ᅭ"
    A50 = "a50ᅭ"
    A5_A = "a5Aᅮ"
    A6 = "a6-ᅲ"
    A60 = "a60ᅲ"
    A6_A = "a6Aᅳ"
    A70 = "a70ᅵ"
    A80 = "a80ᆞ"
    A90 = "a90ᆨ"


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
