from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v05"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v05"

    el_max_exclusive_min_inclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": Duration("-P39DT3M"),
            "max_exclusive": Duration("P28D"),
        }
    )
    el_max_exclusive_min_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": Duration("-P39DT2M"),
            "max_exclusive": Duration("P28D"),
        }
    )
    el_max_exclusive_max_inclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": Duration("P28D"),
            "max_inclusive": Duration("P27DT3M"),
        }
    )
    el_max_exclusive_max_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": Duration("P27D"),
        }
    )
