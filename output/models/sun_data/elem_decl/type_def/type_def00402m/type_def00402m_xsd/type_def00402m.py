from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ComplexType:
    global_value: Optional[Global] = field(
        default=None,
        metadata={
            "name": "Global",
            "type": "Element",
            "namespace": "ElemDecl/typeDef",
            "required": True,
        },
    )
    local: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
