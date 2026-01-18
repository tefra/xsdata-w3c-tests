from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/minOccurs"


@dataclass(kw_only=True)
class Local:
    class Meta:
        namespace = "ElemDecl/minOccurs"

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
        namespace = "ElemDecl/minOccurs"

    local: Local = field(
        metadata={
            "name": "Local",
            "type": "Element",
            "required": True,
        }
    )
