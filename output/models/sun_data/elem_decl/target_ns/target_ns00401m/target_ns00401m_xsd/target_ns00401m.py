from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/targetNS"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
