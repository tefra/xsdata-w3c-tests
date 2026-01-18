from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elt1:
    class Meta:
        name = "elt1"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Elt2:
    class Meta:
        name = "elt2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    elt1: list[Elt1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
