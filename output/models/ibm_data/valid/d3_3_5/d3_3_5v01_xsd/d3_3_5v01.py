from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_5_v01"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_5_v01"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 5.0,
        }
    )
