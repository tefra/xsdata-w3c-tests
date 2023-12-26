from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "SType/ST_facets"


class S(Enum):
    A_A = "a--a"
    B_B = "b..b"
    C_C = "c__c"
    D_D = "d··d"
    E_E = "e··e"
    F_F = "f\u06dd\u06ddf"
    G_G = "g۞۞g"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "SType/ST_facets"

    val: List[S] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 7,
        },
    )
