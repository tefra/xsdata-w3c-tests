from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass
class GlobalType:
    """
    :ivar any_element:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/targetNS"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )