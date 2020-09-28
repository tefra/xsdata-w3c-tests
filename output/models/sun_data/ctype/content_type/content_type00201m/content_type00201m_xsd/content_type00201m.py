from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "contentType"


@dataclass
class A1:
    """
    :ivar value:
    """
    class Meta:
        name = "A"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "contentType"
