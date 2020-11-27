from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BE1:
    class Meta:
        name = "b-e1"
        namespace = "ns-a"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 4,
        }
    )
