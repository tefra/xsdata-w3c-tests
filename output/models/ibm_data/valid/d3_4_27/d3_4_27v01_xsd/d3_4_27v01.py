from dataclasses import dataclass, field
from enum import Enum
from typing import List
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v01"


class YMdenumeration(Enum):
    P2_D = XmlDuration("P2D")
    PT54_H3_M2_3_S = XmlDuration("PT54H3M2.3S")
    P5_DT3_S = XmlDuration("-P5DT3S")
    PT43_M4_2_S = XmlDuration("-PT43M4.2S")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v01"

    ely_mdtype: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDType",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdenumeration: List[YMdenumeration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDEnumeration",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdmin_max_inclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("-P2D"),
            "max_inclusive": XmlDuration("P2D"),
        },
    )
    ely_mdmin_max_exclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": XmlDuration("-P2D"),
            "max_exclusive": XmlDuration("P2D"),
        },
    )
