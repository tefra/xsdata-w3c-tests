from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        nillable = True
        namespace = "ElemDecl/nillable"

    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )
