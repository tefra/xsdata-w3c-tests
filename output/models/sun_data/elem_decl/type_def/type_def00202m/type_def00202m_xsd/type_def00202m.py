from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Root:
    """
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="Element",
            type="Element",
            namespace="",
            required=True
        )
    )
