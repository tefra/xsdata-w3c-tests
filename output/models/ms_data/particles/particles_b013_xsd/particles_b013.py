from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: None | Elem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
