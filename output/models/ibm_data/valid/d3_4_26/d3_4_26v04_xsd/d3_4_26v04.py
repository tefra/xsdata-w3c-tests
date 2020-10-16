from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v04"


@dataclass
class Root:
    """
    :ivar ely_mdmin_inclusive_min_inclusive:
    :ivar ely_mdmin_inclusive_min_exclusive:
    :ivar ely_mdmin_inclusive_max_inclusive:
    :ivar ely_mdmin_inclusive_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v04"

    ely_mdmin_inclusive_min_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "P2M",
        }
    )
    ely_mdmin_inclusive_min_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": "P2M",
            "min_inclusive": "P1M",
        }
    )
    ely_mdmin_inclusive_max_inclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "P1M",
            "max_inclusive": "P3452Y2M",
        }
    )
    ely_mdmin_inclusive_max_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "P1M",
            "max_exclusive": "P23Y2M",
        }
    )
