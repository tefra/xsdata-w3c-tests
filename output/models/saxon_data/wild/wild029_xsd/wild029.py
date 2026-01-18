from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Eden:
    class Meta:
        name = "eden"

    a: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 3,
            "sequence": 1,
        },
    )
    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        },
    )
