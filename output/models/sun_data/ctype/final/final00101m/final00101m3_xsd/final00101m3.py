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
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class B(A):
    """
    :ivar d:
    """
    d: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class B(B):
    class Meta:
        name = "b"
        namespace = "final"
