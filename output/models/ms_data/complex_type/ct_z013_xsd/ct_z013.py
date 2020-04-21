from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns"


@dataclass
class Ct:
    """
    :ivar content:
    :ivar a:
    """
    class Meta:
        name = "CT"

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    a: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class E(Ct):
    class Meta:
        name = "e"
        namespace = "ns"
