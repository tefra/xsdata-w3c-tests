from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/maxOccurs"


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/maxOccurs"

    local: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            namespace="",
            required=True
        )
    )
