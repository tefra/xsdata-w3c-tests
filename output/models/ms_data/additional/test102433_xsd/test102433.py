from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "q"


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"
        namespace = "q"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
