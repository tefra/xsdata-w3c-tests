from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Element:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1|0",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[Element] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "required": True,
        },
    )
