from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Global:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"false",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"false",
        }
    )
