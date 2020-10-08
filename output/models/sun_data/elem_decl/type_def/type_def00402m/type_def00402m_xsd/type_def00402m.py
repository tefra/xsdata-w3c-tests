from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class ComplexType:
    """
    :ivar global_value:
    :ivar local:
    """
    global_value: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Global",
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
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
