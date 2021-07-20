from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Local:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    local: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
        }
    )
