from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class Z:
    class Meta:
        name = "z"
        namespace = "a"

    value: int = field()


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    z: None | Z = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "a",
        },
    )
    any_element: None | object = field(
        default=None,
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
