from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    """
    :cvar A_A:
    :cvar B_B:
    :cvar C_C:
    :cvar D_D:
    :cvar E_E:
    :cvar F_F:
    :cvar G_G:
    """
    A_A = "a--a"
    B_B = "b..b"
    C_C = "c__c"
    D_D = "d··d"
    E_E = "e··e"
    F_F = "f۝۝f"
    G_G = "g۞۞g"


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
            max_occurs=7
        )
    )
