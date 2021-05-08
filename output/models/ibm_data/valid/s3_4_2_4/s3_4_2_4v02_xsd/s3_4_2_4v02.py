from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"

    e1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
