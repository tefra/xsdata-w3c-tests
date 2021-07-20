from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/abstract"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/abstract"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
