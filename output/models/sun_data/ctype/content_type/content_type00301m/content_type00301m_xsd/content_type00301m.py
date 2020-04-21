from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A:
    """
    :ivar b:
    """
    b: Optional[str] = field(
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
