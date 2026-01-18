from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ComplexType:
    global_value: Global = field(
        metadata={
            "name": "Global",
            "type": "Element",
            "namespace": "ElemDecl/typeDef",
            "required": True,
        }
    )
    local: Decimal = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
