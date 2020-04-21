from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A:
    """
    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "contentType"
