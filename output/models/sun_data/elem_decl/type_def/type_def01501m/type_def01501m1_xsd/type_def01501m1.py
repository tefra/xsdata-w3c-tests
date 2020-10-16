from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Text:
    """
    :ivar content:
    :ivar dot:
    :ivar id:
    """
    class Meta:
        name = "text"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    dot: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )


@dataclass
class Root(Text):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
