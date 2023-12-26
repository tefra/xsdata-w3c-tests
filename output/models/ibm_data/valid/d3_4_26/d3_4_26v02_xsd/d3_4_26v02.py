from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v02"


class YMdenumeration(Enum):
    P1_Y = XmlDuration("P1Y")
    P1_Y3_M = XmlDuration("P1Y3M")
    P34_Y233_M = XmlDuration("-P34Y233M")
    P45_M = XmlDuration("P45M")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    ay_mdtype: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ayMDType",
            "type": "Attribute",
        },
    )
    ay_mdenumeration: Optional[YMdenumeration] = field(
        default=None,
        metadata={
            "name": "ayMDEnumeration",
            "type": "Attribute",
        },
    )
    ay_mdmin_max_inclusive: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": XmlDuration("-P2Y"),
            "max_inclusive": XmlDuration("P30Y23M"),
        },
    )
    ay_mdmin_max_exclusive: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": XmlDuration("-P2Y"),
            "max_exclusive": XmlDuration("P30Y23M"),
        },
    )
