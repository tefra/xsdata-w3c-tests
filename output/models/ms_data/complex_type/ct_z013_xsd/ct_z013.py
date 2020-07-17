from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ns"


@dataclass
class Ct:
    """
    :ivar content:
    :ivar a:
    """
    class Meta:
        name = "CT"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
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
