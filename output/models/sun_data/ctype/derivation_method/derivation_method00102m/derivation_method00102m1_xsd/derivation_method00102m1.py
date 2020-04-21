from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A:
    """
    :ivar value:
    """
    value: Optional[int] = field(
        default=None,
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "derivationMethod"
