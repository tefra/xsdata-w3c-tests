from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    e1: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_exclusive": 2,
            "min_inclusive": 2,
        }
    )
    e2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_exclusive": 2,
            "min_inclusive": 3,
        }
    )


@dataclass(kw_only=True)
class Root(Ct):
    pass
