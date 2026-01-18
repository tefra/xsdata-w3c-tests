from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Text:
    class Meta:
        name = "text"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class Root(Text):
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"
