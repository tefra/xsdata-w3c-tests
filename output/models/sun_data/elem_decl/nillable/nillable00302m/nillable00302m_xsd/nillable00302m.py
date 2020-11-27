from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/nillable"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        }
    )
