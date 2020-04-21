from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/minOccurs"


@dataclass
class Local:
    """
    :ivar any_element:
    """
    class Meta:
        namespace = "ElemDecl/minOccurs"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/minOccurs"

    local: Optional[Local] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            required=True
        )
    )
