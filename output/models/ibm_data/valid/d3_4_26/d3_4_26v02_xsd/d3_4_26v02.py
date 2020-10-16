from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v02"


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
    :ivar value:
    :ivar ay_mdtype:
    :ivar ay_mdenumeration:
    :ivar ay_mdmin_max_inclusive:
    :ivar ay_mdmin_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v02"

    value: Optional[str] = field(
        default=None,
    )
    ay_mdtype: Optional[str] = field(
        default=None,
        metadata={
            "name": "ayMDType",
            "type": "Attribute",
        }
    )
    ay_mdenumeration: Optional[YMdenumeration] = field(
        default=None,
        metadata={
            "name": "ayMDEnumeration",
            "type": "Attribute",
        }
    )
    ay_mdmin_max_inclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": "-P2Y",
            "max_inclusive": "P30Y23M",
        }
    )
    ay_mdmin_max_exclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": "-P2Y",
            "max_exclusive": "P30Y23M",
        }
    )
