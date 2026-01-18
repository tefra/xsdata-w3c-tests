from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ElemDecl/name"


@dataclass(kw_only=True)
class Main:
    class Meta:
        namespace = "ElemDecl/name"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


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


@dataclass(kw_only=True)
class Global:
    class Meta:
        namespace = "ElemDecl/name"

    main: list[Main] = field(
        default_factory=list,
        metadata={
            "name": "Main",
            "type": "Element",
            "min_occurs": 1,
        },
    )
