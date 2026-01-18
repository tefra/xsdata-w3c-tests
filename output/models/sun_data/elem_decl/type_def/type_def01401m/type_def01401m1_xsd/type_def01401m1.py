from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/typeDef"

    value: None | int = field(
        metadata={
            "nillable": True,
        }
    )
