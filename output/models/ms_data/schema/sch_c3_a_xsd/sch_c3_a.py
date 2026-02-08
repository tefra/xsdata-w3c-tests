from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class CtA:
    class Meta:
        name = "ct-A"

    a1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    a2: bool = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E1(CtA):
    class Meta:
        name = "e1"
