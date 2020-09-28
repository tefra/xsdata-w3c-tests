from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "attributeUses"


@dataclass
class A1:
    """
    :ivar value:
    :ivar attr1:
    :ivar attr2:
    """
    class Meta:
        name = "A"

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
class A(A1):
    class Meta:
        name = "a"
        namespace = "attributeUses"
