from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"false",
        }
    )
