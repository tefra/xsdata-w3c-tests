from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class ComplexType:
    """
    :ivar in_value:
    :ivar out:
    :ivar add:
    :ivar tail:
    """
    class Meta:
        name = "complexType"

    in_value: Optional[object] = field(
        default=None,
        metadata=dict(
            name="in",
            type="Element",
            namespace="foo",
            required=True
        )
    )
    out: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )
    add: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    tail: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="foo",
            required=True
        )
    )


class SimpleType(Enum):
    """
    :cvar NO:
    :cvar YES:
    """
    NO = "no"
    YES = "yes"
