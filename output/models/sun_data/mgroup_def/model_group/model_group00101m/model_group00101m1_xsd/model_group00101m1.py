from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "modelGroup"


@dataclass
class A1:
    """
    :ivar c:
    :ivar date:
    """
    class Meta:
        name = "A"

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
class A(A1):
    class Meta:
        name = "a"
        namespace = "modelGroup"
