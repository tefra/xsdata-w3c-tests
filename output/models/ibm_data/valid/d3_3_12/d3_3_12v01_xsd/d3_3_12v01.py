from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_12_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_12_v01"

    el_date: List[str] = field(
        default_factory=list,
        metadata={
            "name": "elDate",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": "2000+13:00",
        }
    )
