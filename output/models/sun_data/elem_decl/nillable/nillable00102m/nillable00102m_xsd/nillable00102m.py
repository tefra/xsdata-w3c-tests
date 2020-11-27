from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/nillable"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
