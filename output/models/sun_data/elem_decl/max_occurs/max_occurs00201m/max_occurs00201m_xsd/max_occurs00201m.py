from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/maxOccurs"


@dataclass(kw_only=True)
class Local:
    class Meta:
        namespace = "ElemDecl/maxOccurs"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/maxOccurs"

    local: Local = field(
        metadata={
            "name": "Local",
            "type": "Element",
        }
    )
