from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: Optional[bool] = field(
        default=None
    )
