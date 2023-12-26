from dataclasses import dataclass, field
from typing import List, Union
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v06"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v06"

    union_element: List[Union[XmlDate, int, str]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[a-z][x-z]",
        },
    )
