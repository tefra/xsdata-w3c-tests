from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    total1: int = field(
        metadata={
            "name": "Total1",
            "type": "Element",
            "namespace": "",
            "total_digits": 3,
        }
    )
    total2: int = field(
        metadata={
            "name": "Total2",
            "type": "Element",
            "namespace": "",
            "min_exclusive": 100,
            "total_digits": 3,
        }
    )
