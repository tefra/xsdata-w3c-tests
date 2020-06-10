from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A:
    pass


@dataclass
class B(A):
    """
    :ivar q:
    """
    q: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class B(B):
    class Meta:
        name = "b"
        namespace = "derivationMethod"
