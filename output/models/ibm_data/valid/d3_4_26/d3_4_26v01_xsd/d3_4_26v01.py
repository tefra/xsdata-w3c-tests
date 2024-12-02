from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v01"


class YMdenumeration(Enum):
    P1_Y = XmlDuration("P1Y")
    P1_Y3_M = XmlDuration("P1Y3M")
    P34_Y233_M = XmlDuration("-P34Y233M")
    P45_M = XmlDuration("P45M")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v01"

    ely_mdtype: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDType",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdenumeration: list[YMdenumeration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDEnumeration",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    ely_mdmin_max_inclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("-P2Y"),
            "max_inclusive": XmlDuration("P30Y23M"),
        },
    )
    ely_mdmin_max_exclusive: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": XmlDuration("-P2Y"),
            "max_exclusive": XmlDuration("P30Y23M"),
        },
    )
