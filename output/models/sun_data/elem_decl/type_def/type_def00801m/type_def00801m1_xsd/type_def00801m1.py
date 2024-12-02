from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Type:
    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DerivedType(Type):
    class Meta:
        name = "derivedType"

    value1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[Type] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
