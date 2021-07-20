from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/name"

    root: Optional[Root] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
