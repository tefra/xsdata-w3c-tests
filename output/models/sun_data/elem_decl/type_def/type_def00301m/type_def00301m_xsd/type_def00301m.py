from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Local:
    class Meta:
        namespace = "ElemDecl/typeDef"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    local: Local = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "required": True,
        }
    )
