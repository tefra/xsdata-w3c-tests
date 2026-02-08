from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/term"


@dataclass(kw_only=True)
class Local:
    class Meta:
        namespace = "ElemDecl/term"

    value: bool = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/term"

    local: Local = field(
        metadata={
            "name": "Local",
            "type": "Element",
        }
    )
