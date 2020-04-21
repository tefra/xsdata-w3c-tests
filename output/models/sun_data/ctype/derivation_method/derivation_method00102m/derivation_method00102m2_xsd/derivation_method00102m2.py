from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "derivationMethod"


@dataclass
class A:
    """
    :ivar value:
    :ivar t:
    """
    value: Optional[int] = field(
        default=None,
    )
    t: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "derivationMethod"
