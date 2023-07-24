from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass
class Text:
    class Meta:
        name = "text"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Root(Text):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
