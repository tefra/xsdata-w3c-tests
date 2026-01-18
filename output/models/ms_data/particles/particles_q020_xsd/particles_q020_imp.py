from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "foo"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
