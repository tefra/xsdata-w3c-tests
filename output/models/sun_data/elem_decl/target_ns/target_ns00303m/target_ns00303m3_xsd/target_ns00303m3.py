from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/targetNS"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
