from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar AA111A2_AA:
    :cvar AA22_B3C:
    :cvar AA3_4:
    """
    AA111A2_AA = "aa111a2Aa"
    AA22_B3C = "aa22B3c"
    AA3_4 = "aa3-4_"


@dataclass
class Root:
    """
    :ivar val:
    """
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=3
        )
    )
