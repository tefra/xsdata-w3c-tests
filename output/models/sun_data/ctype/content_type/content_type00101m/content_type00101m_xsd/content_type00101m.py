from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A:
    """
    :ivar attr1:
    """
    attr1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "contentType"
