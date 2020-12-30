from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Duration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v02"


class YMdenumeration(Enum):
    P1_Y = Duration("P1Y")
    P1_Y3_M = Duration("P1Y3M")
    VALUE_P34_Y233_M = Duration("-P34Y233M")
    P45_M = Duration("P45M")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v02"

    value: Optional[str] = field(
        default=None,
    )
    ay_mdtype: Optional[Duration] = field(
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
    ay_mdmin_max_inclusive: Optional[Duration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": Duration("-P2Y"),
            "max_inclusive": Duration("P30Y23M"),
        }
    )
    ay_mdmin_max_exclusive: Optional[Duration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": Duration("-P2Y"),
            "max_exclusive": Duration("P30Y23M"),
        }
    )
