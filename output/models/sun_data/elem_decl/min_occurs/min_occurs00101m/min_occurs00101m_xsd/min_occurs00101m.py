from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/minOccurs"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/minOccurs"

    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )
