from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"

    a: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class D(C):
    class Meta:
        name = "d"
