from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/scope"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/scope"

    local_element1: None | object = field(
        default=None,
        metadata={
            "name": "LocalElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    local_element2: None | object = field(
        default=None,
        metadata={
            "name": "LocalElement2",
            "type": "Element",
            "namespace": "",
        },
    )
