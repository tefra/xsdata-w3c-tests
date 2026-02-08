from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/typeDef"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/typeDef"

    element: bool = field(
        metadata={
            "name": "Element",
            "type": "Element",
            "namespace": "",
        }
    )
