from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/scope"


@dataclass
class Root:
    """
    :ivar local:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/scope"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
