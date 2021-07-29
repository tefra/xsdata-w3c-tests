from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "d"


@dataclass
class D:
    class Meta:
        name = "d"

    d: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "d",
        }
    )
