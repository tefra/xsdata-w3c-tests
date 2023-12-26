from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "foo"


class SimpleType(Enum):
    YES = "yes"
    NO = "no"


@dataclass
class ComplexType:
    class Meta:
        name = "complexType"

    in_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
            "namespace": "foo",
        },
    )
    root: List["Root"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    out: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    g_att: Optional[SimpleType] = field(
        default=None,
        metadata={
            "name": "gAtt",
            "type": "Attribute",
            "namespace": "foo",
        },
    )
    add: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tail: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
