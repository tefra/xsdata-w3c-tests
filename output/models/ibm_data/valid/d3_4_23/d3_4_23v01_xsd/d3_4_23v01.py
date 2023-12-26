from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11"

    ele: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
