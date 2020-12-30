from dataclasses import dataclass, field
from enum import Enum
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v01"


class YMdenumeration(Enum):
    P2_D = Duration("P2D")
    PT54_H3_M2_3_S = Duration("PT54H3M2.3S")
    VALUE_P5_DT3_S = Duration("-P5DT3S")
    VALUE_PT43_M4_2_S = Duration("-PT43M4.2S")


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v01"

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
            "min_inclusive": Duration("-P2D"),
            "max_inclusive": Duration("P2D"),
        }
    )
    ely_mdmin_max_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": Duration("-P2D"),
            "max_exclusive": Duration("P2D"),
        }
    )
