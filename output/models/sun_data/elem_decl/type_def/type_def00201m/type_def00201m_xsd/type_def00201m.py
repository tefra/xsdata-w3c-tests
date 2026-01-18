from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[01]+",
        },
    )
