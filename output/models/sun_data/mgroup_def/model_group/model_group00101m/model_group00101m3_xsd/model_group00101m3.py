from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "modelGroup"


@dataclass
class A:
    """
    :ivar c:
    :ivar date:
    """
    c: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "modelGroup"
