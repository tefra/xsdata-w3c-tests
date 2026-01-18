from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e: list[bool | int | str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 3,
            "max_occurs": 3,
        },
    )
