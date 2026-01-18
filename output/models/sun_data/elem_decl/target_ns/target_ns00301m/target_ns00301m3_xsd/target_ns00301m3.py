from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/targetNS"

    local: None | object = field(
        default=None,
        metadata={
            "name": "Local",
            "type": "Element",
            "namespace": "",
        },
    )
