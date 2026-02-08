from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
