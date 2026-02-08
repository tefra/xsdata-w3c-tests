from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "final"


@dataclass(kw_only=True)
class A:
    c: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class B1(A):
    class Meta:
        name = "B"

    d: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class B(B1):
    class Meta:
        name = "b"
        namespace = "final"
