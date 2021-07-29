from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/minOccurs"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/minOccurs"

    local: Optional[object] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        }
    )
