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
class GlobalPreDefinedType:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1|true",
        },
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
    global_pre_defined_type: GlobalPreDefinedType = field(
        metadata={
            "name": "GlobalPreDefinedType",
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
    local_pre_defined_type: str = field(
        metadata={
            "name": "LocalPreDefinedType",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"1|true",
        }
    )
    local_inline: str = field(
        metadata={
            "name": "LocalInline",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"0|false",
        }
    )


@dataclass(kw_only=True)
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
