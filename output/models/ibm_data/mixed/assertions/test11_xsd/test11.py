from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xyz"


@dataclass
class X:
    class Meta:
        namespace = "http://xyz"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
