from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A10:
    :cvar A20:
    :cvar A30:
    :cvar A40:
    :cvar A50:
    :cvar A60:
    :cvar A70:
    :cvar A80:
    :cvar A8:
    :cvar A8_A:
    :cvar A90:
    :cvar A9:
    :cvar A9_A:
    """
    A00 = "a00·"
    A10 = "a10ː"
    A20 = "a20ˑ"
    A30 = "a30·"
    A40 = "a40ـ"
    A50 = "a50ๆ"
    A60 = "a60ໆ"
    A70 = "a70々"
    A80 = "a80〱"
    A8 = "a8-〳"
    A8_A = "a8A〵"
    A90 = "a90ゝ"
    A9 = "a9-ゝ"
    A9_A = "a9Aゞ"


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
