from dataclasses import dataclass, field
from enum import Enum
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v01"


class YMdenumeration(Enum):
    P1_Y = Duration("P1Y")
    P1_Y3_M = Duration("P1Y3M")
    VALUE_P34_Y233_M = Duration("-P34Y233M")
    P45_M = Duration("P45M")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v01"

    ely_mdtype: List[Duration] = field(
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
    ely_mdmin_max_inclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": Duration("-P2Y"),
            "max_inclusive": Duration("P30Y23M"),
        }
    )
    ely_mdmin_max_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": Duration("-P2Y"),
            "max_exclusive": Duration("P30Y23M"),
        }
    )
