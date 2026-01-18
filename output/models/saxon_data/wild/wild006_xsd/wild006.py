from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Eden:
    class Meta:
        name = "eden"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
