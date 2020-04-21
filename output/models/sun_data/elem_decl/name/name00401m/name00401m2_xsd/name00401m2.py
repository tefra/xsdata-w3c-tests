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
class GlobalType:
    """
    :ivar root:
    """
    class Meta:
        name = "Global"
        namespace = "ElemDecl/name"

    root: Optional[Root] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
