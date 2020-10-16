from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v05"


@dataclass
class Root:
    """
    :ivar el_max_exclusive_min_inclusive:
    :ivar el_max_exclusive_min_exclusive:
    :ivar el_max_exclusive_max_inclusive:
    :ivar el_max_exclusive_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v05"

    el_max_exclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "-P39Y3M",
            "max_exclusive": "P28Y",
        }
    )
    el_max_exclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": "-P39Y2M",
            "max_exclusive": "P28Y",
        }
    )
    el_max_exclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": "P28Y",
            "max_inclusive": "P27Y3M",
        }
    )
    el_max_exclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": "P27Y",
        }
    )
