from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/typeDef"

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
