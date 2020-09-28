from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A:
    pass


@dataclass
class B1(A):
    """
    :ivar q:
    """
    class Meta:
        name = "B"

    q: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class B(B1):
    class Meta:
        name = "b"
        namespace = "derivationMethod"
