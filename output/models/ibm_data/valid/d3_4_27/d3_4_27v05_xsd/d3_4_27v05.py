from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_27_v05"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_27_v05"

    el_max_exclusive_min_inclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDuration("-P39DT3M"),
            "max_exclusive": XmlDuration("P28D"),
        },
    )
    el_max_exclusive_min_exclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MinExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": XmlDuration("-P39DT2M"),
            "max_exclusive": XmlDuration("P28D"),
        },
    )
    el_max_exclusive_max_inclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": XmlDuration("P28D"),
            "max_inclusive": XmlDuration("P27DT3M"),
        },
    )
    el_max_exclusive_max_exclusive: List[XmlDuration] = field(
        default_factory=list,
        metadata={
            "name": "elMaxExclusive_MaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_exclusive": XmlDuration("P27D"),
        },
    )
