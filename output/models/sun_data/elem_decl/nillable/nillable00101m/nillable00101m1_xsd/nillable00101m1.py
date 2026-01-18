from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/nillable"

    value: None | bool = field(
        metadata={
            "nillable": True,
        }
    )
