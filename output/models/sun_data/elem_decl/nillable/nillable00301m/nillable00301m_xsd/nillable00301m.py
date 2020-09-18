from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/nillable"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
