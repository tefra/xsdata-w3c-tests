from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/scope"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/scope"

    local_element1: Optional[object] = field(
        default=None,
        metadata={
            "name": "LocalElement1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_element2: Optional[object] = field(
        default=None,
        metadata={
            "name": "LocalElement2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
