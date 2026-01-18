from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "foo"


class SimpleType(Enum):
    YES = "yes"
    NO = "no"


@dataclass(kw_only=True)
class ComplexType:
    class Meta:
        name = "complexType"

    in_value: None | object = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
            "namespace": "foo",
        },
    )
    root: list[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    out: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )
    g_att: None | SimpleType = field(
        default=None,
        metadata={
            "name": "gAtt",
            "type": "Attribute",
            "namespace": "foo",
        },
    )
    add: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tail: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "foo",
        },
    )


@dataclass(kw_only=True)
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
