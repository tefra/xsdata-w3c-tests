from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class TypeType:
    class Meta:
        name = "Type"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DerivedType(TypeType):
    class Meta:
        name = "derivedType"

    value1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[TypeType] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
