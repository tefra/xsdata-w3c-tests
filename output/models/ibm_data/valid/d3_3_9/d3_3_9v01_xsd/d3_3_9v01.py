from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_9_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_9_v01"

    el_time1: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "elTime1",
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlTime(8, 0, 0, 0, 600),
        },
    )
    el_time2: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "elTime2",
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlTime(0, 0, 0, 0, 60),
        },
    )
    el_time3: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "elTime3",
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlTime(10, 0, 0, 0, 780),
        },
    )
    el_time4: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "elTime4",
            "type": "Element",
            "namespace": "",
            "min_inclusive": XmlTime(3, 0, 0, 0, 240),
        },
    )
