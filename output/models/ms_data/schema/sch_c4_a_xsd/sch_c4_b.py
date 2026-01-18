from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class CtB:
    class Meta:
        name = "ct-B"

    b1: bool = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )
    b2: int = field(
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"
