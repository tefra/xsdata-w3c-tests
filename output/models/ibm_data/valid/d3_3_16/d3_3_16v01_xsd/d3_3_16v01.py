from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    ele: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_length": 4,
            "format": "base16",
        }
    )
