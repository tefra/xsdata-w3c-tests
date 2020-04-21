from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "attributeUses"


@dataclass
class A:
    """
    :ivar value:
    :ivar attr1:
    :ivar attr2:
    """
    value: Optional[int] = field(
        default=None,
    )
    attr1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    attr2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class A(A):
    class Meta:
        name = "a"
        namespace = "attributeUses"
