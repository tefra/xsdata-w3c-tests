from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Boolean:
    """
    :ivar value:
    """
    class Meta:
        name = "boolean"

    value: Optional[bool] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
