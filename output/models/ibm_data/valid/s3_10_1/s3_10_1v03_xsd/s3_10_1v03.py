from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    q_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "q",
        },
    )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
