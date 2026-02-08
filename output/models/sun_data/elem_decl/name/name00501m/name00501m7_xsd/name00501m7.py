from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/name"

    local: bool = field(
        metadata={
            "name": "Local",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Main:
    class Meta:
        namespace = "ElemDecl/name"

    value: bool = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ElemDecl/name"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
