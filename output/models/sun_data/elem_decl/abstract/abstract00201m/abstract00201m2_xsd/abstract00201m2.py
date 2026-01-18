from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/abstract"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/abstract"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
