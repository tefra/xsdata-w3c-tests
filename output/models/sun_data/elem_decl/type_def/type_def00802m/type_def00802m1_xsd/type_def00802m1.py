from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Element:
    """
    :ivar value:
    """
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"1|0",
        }
    )


@dataclass
class Root:
    """
    :ivar element:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: Optional[str] = field(
        default=None,
        metadata={
            "name": "Element",
            "type": "Element",
            "required": True,
            "pattern": r"1|0",
        }
    )
