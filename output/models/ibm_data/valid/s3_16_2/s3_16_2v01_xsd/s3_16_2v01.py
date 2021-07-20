from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/IBMd3_16v02"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/IBMd3_16v02"

    elflt_union_c: List[float] = field(
        default_factory=list,
        metadata={
            "name": "elfltUnionC",
            "type": "Element",
            "namespace": "",
            "min_inclusive": -12.0,
            "max_inclusive": 12.0,
        }
    )
