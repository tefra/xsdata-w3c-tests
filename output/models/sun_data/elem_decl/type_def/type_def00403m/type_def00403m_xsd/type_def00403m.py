from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class GlobalType:
    """
    :ivar value:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class GlobalPreDefinedType:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"1|true"
        )
    )


@dataclass
class ComplexType:
    """
    :ivar global_value:
    :ivar global_pre_defined_type:
    :ivar local:
    :ivar local_pre_defined_type:
    :ivar local_inline:
    """
    global_value: Optional[GlobalType] = field(
        default=None,
        metadata=dict(
            name="Global",
            type="Element",
            namespace="ElemDecl/typeDef",
            required=True
        )
    )
    global_pre_defined_type: Optional[GlobalPreDefinedType] = field(
        default=None,
        metadata=dict(
            name="GlobalPreDefinedType",
            type="Element",
            namespace="ElemDecl/typeDef",
            required=True
        )
    )
    local: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
            required=True
        )
    )
    local_pre_defined_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LocalPreDefinedType",
            type="Element",
            namespace="",
            required=True,
            pattern=r"1|true"
        )
    )
    local_inline: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LocalInline",
            type="Element",
            namespace="",
            required=True,
            pattern=r"0|false"
        )
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
