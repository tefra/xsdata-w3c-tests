from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/targetNS"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
