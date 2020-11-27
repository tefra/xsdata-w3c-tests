from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "b"


@dataclass
class B:
    class Meta:
        name = "b"

    b: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "b",
            "required": True,
        }
    )
