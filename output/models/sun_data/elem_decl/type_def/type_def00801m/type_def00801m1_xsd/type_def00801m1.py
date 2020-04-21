from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Type:
    """
    :ivar value:
    """
    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class DerivedType(Type):
    """
    :ivar value1:
    """
    class Meta:
        name = "derivedType"

    value1: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[Type] = field(
        default=None,
        metadata=dict(
            name="Element",
            type="Element",
            namespace="",
            required=True
        )
    )
