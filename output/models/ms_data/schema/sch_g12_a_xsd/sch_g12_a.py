from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class FooA:
    class Meta:
        name = "foo_a"
        namespace = "ns-a"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
