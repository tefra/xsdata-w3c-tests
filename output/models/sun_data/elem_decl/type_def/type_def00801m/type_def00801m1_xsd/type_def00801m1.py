from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Type:
    value: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DerivedType(Type):
    class Meta:
        name = "derivedType"

    value1: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Type = field(
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        }
    )
