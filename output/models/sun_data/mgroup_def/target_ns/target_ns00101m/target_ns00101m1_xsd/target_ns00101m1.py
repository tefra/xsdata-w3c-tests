from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "targetNS0"


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
            namespace=""
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "targetNS0"