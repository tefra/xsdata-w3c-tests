from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/nillable"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/nillable"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
