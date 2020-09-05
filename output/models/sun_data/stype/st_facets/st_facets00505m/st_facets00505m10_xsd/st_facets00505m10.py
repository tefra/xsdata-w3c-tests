from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A00:
    :cvar A0:
    :cvar A0_A:
    :cvar A10:
    :cvar A20:
    :cvar A2:
    :cvar A2_A:
    :cvar A30:
    :cvar A40:
    """
    A00 = "a00⃐"
    A0 = "a0-⃖"
    A0_A = "a0A⃜"
    A10 = "a10⃡"
    A20 = "a20〪"
    A2 = "a2-〬"
    A2_A = "a2A〯"
    A30 = "a30゙"
    A40 = "a40゚"


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
