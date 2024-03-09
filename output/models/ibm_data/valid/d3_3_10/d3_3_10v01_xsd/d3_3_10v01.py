from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_10_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_10_v01"

    el_date: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "name": "elDate",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": XmlDate(2000, 12, 12, 780),
        },
    )
