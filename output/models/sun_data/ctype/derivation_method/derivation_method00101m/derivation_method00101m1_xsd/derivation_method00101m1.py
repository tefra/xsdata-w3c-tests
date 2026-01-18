from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "derivationMethod"


@dataclass(kw_only=True)
class A:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class B1(A):
    class Meta:
        name = "B"

    q: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class B(B1):
    class Meta:
        name = "b"
        namespace = "derivationMethod"
