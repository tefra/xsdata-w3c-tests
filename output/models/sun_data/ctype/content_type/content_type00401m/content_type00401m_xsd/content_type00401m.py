from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "contentType"


@dataclass
class A:
    """
    :ivar content:
    :ivar date:
    """
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
        namespace = "contentType"
