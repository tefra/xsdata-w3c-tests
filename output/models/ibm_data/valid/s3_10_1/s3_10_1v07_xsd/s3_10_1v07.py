from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    a_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "a",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class X:
    class Meta:
        name = "x"
        namespace = "a"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
