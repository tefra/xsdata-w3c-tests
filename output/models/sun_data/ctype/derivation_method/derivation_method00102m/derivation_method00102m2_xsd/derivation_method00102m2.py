from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A1:
    class Meta:
        name = "A"

    value: Optional[int] = field(
        default=None,
    )
    t: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "derivationMethod"
