from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v02"


class YMdenumeration(Enum):
    P1_D = XmlDuration("P1D")
    P3_DT44_H2_M = XmlDuration("P3DT44H2M")
    P3_DT44_H2_M5783_33_S = XmlDuration("-P3DT44H2M5783.33S")
    P5_DT0_H0_3_S = XmlDuration("P5DT0H0.3S")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v02"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    ay_mdtype: Optional[XmlDuration] = field(
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
    ay_mdmin_max_inclusive: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": XmlDuration("-P2D"),
            "max_inclusive": XmlDuration("P30DT400H"),
        }
    )
    ay_mdmin_max_exclusive: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": XmlDuration("-P2D"),
            "max_exclusive": XmlDuration("P30DT400H"),
        }
    )
