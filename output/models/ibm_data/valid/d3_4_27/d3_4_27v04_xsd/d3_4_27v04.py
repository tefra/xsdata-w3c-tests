from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import Duration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v04"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v04"

    ely_mdmin_inclusive_min_inclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": Duration("P1DT535.4S"),
        }
    )
    ely_mdmin_inclusive_min_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": Duration("P2D"),
            "min_inclusive": Duration("P1D"),
        }
    )
    ely_mdmin_inclusive_max_inclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": Duration("P1D"),
            "max_inclusive": Duration("P3452DT2H"),
        }
    )
    ely_mdmin_inclusive_max_exclusive: List[Duration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": Duration("P1D"),
            "max_exclusive": Duration("P43DT43M"),
        }
    )
