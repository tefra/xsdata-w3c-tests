from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.example.org"


@dataclass
class X:
    class Meta:
        name = "x"
        namespace = "http://www.example.org"

    y: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
