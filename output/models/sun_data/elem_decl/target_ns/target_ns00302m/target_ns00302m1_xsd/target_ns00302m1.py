from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/targetNS"

    local: Optional[object] = field(
        default=None,
        metadata=dict(
            name="Local",
            type="Element",
            required=True
        )
    )
