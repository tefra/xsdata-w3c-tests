from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Example:
    x: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    kind: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
