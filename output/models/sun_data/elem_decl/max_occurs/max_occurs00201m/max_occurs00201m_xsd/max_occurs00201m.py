from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/maxOccurs"


@dataclass
class Local:
    class Meta:
        namespace = "ElemDecl/maxOccurs"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/maxOccurs"

    local: Optional[Local] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "required": True,
        },
    )
