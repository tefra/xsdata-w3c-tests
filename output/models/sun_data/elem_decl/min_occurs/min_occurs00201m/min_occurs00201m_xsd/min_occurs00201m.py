from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/minOccurs"


@dataclass
class Local:
    class Meta:
        namespace = "ElemDecl/minOccurs"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/minOccurs"

    local: Optional[Local] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "required": True,
        }
    )
