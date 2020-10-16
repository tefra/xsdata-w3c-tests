from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v01"


class YMdenumeration(Enum):
    """
    :cvar P1_Y:
    :cvar P1_Y3_M:
    :cvar P34_Y233_M:
    :cvar P45_M:
    """
    P1_Y = "P1Y"
    P1_Y3_M = "P1Y3M"
    P34_Y233_M = "-P34Y233M"
    P45_M = "P45M"


@dataclass
class Root:
    """
    :ivar ely_mdtype:
    :ivar ely_mdenumeration:
    :ivar ely_mdmin_max_inclusive:
    :ivar ely_mdmin_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v01"

    ely_mdtype: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDType",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    ely_mdenumeration: List[YMdenumeration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDEnumeration",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    ely_mdmin_max_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "-P2Y",
            "max_inclusive": "P30Y23M",
        }
    )
    ely_mdmin_max_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": "-P2Y",
            "max_exclusive": "P30Y23M",
        }
    )
