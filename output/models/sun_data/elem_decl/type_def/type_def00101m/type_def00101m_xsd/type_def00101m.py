from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Answer:
    class Meta:
        name = "answer"
        namespace = "ElemDecl/typeDef"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
