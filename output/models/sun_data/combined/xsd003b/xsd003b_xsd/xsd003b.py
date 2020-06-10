from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


class SimpleType(Enum):
    """
    :cvar YES:
    :cvar NO:
    """
    YES = "yes"
    NO = "no"


@dataclass
class ComplexType:
    """
    :ivar in_value:
    :ivar root:
    :ivar out:
    :ivar g_att:
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
    root: List["Root"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="foo",
            min_occurs=0,
            max_occurs=9223372036854775807
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
    g_att: Optional[SimpleType] = field(
        default=None,
        metadata=dict(
            name="gAtt",
            type="Attribute",
            namespace="foo"
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
