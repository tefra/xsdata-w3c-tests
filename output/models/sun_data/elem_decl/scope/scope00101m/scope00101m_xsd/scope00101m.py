from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/scope"


@dataclass
class GlobalType:
    class Meta:
        name = "Global"
        namespace = "ElemDecl/scope"

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
        namespace = "ElemDecl/scope"

    global_value: Optional[GlobalType] = field(
        default=None,
        metadata={
            "name": "Global",
            "type": "Element",
            "required": True,
        }
    )
    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
