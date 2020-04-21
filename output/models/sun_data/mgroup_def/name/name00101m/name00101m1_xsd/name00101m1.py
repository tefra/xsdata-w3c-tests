from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "name"


@dataclass
class A:
    """
    :ivar c:
    """
    c: Optional[int] = field(
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
        namespace = "name"
