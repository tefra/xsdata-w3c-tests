from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-b"


@dataclass
class CtA:
    """
    :ivar a1:
    :ivar a2:
    """
    class Meta:
        name = "ct-A"

    a1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    a2: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-b"
