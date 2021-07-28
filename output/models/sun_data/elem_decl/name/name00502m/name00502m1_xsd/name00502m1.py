from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Global1:
    class Meta:
        namespace = "ElemDecl/name"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Global2:
    class Meta:
        namespace = "ElemDecl/name"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


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
            "required": True,
        }
    )
