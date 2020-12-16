from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v02"


class YMdenumeration(Enum):
    P1_D = "P1D"
    P3_DT44_H2_M = "P3DT44H2M"
    VALUE_P3_DT44_H2_M5783_33_S = "-P3DT44H2M5783.33S"
    P5_DT0_H0_3_S = "P5DT0H0.3S"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v02"

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
            "min_inclusive": "-P2D",
            "max_inclusive": "P30DT400H",
        }
    )
    ay_mdmin_max_exclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "ayMDMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": "-P2D",
            "max_exclusive": "P30DT400H",
        }
    )
