from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    element1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
        },
    )
