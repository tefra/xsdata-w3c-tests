from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e1: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
