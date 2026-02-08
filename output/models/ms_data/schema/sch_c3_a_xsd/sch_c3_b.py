from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class CtB:
    class Meta:
        name = "ct-B"

    b1: bool = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    b2: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class E2(CtB):
    class Meta:
        name = "e2"
