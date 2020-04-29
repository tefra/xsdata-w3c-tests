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

    content: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any"
        )
    )
    dot: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ID",
            type="Attribute"
        )
    )


@dataclass
class Root(Text):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
