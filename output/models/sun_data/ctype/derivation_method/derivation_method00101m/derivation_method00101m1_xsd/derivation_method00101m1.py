from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class B1:
    class Meta:
        name = "B"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    q: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class B(B1):
    class Meta:
        name = "b"
        namespace = "derivationMethod"
