from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E:
    class Meta:
        name = "e"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
