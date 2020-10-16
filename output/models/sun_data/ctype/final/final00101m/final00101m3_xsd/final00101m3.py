from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "final"


@dataclass
class A:
    """
    :ivar c:
    """
    c: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class B1(A):
    """
    :ivar d:
    """
    class Meta:
        name = "B"

    d: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class B(B1):
    class Meta:
        name = "b"
        namespace = "final"
