from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Type1:
    """
    :ivar local:
    """
    class Meta:
        name = "type1"

    local: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class Type2:
    """
    :ivar local:
    """
    class Meta:
        name = "type2"

    local: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
            required=True
        )
    )