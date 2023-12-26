from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_13_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_13_v01"

    el_date: List[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "name": "elDate",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlPeriod("--12-12+13:00"),
        },
    )
