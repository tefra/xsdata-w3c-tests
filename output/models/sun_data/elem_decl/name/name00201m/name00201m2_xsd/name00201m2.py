from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    value: str = field(
        default="",
        metadata={
            "pattern": r"false",
        },
    )
