from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "abstract"


@dataclass
class A:
    c: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class B1(A):
    class Meta:
        name = "B"

    d: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class B(B1):
    class Meta:
        name = "b"
        namespace = "abstract"
