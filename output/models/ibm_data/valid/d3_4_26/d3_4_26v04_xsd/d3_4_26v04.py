from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_26_v04"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_26_v04"

    ely_mdmin_inclusive_min_inclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P2M"),
        },
    )
    ely_mdmin_inclusive_min_exclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": XmlDuration("P2M"),
            "min_inclusive": XmlDuration("P1M"),
        },
    )
    ely_mdmin_inclusive_max_inclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P1M"),
            "max_inclusive": XmlDuration("P3452Y2M"),
        },
    )
    ely_mdmin_inclusive_max_exclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elyMDMinInclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("P1M"),
            "max_exclusive": XmlDuration("P23Y2M"),
        },
    )
