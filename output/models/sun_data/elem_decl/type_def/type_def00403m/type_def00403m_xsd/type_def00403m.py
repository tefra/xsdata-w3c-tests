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
    global_pre_defined_type: Optional[GlobalPreDefinedType] = field(
        default=None,
        metadata={
            "name": "GlobalPreDefinedType",
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
    local_pre_defined_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalPreDefinedType",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"1|true",
        },
    )
    local_inline: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocalInline",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"0|false",
        },
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
