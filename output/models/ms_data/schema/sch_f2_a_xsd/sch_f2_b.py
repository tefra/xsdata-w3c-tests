from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-b"


@dataclass(kw_only=True)
class CtA:
    class Meta:
        name = "ct-A"

    a1: bool = field(
        metadata={
            "type": "Element",
            "namespace": "ns-b",
        }
    )
    a2: int = field(
        metadata={
            "type": "Element",
            "namespace": "ns-b",
        }
    )


@dataclass(kw_only=True)
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-b"
