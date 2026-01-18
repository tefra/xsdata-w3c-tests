from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-b"


@dataclass(kw_only=True)
class FooB:
    class Meta:
        name = "foo_b"
        namespace = "ns-b"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
