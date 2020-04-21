from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "abstract"


@dataclass
class B:
    """
    :ivar c:
    :ivar d:
    """
    c: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    d: Optional[int] = field(
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
        namespace = "abstract"
