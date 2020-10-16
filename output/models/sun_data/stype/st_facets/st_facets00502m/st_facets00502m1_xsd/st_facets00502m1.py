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
    """
    A00 = "a00一"
    A0 = "a0-盒"
    A0_A = "a0A龥"
    A10 = "a10〇"
    A20 = "a20〡"
    A2 = "a2-〥"
    A2_A = "a2A〩"


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
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
