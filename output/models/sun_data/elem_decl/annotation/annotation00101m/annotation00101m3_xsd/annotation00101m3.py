from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/annotation"


@dataclass(kw_only=True)
class Test:
    class Meta:
        namespace = "ElemDecl/annotation"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/annotation"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
