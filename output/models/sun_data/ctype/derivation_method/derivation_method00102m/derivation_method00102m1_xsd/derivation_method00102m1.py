from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "derivationMethod"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "A"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class A(A1):
    class Meta:
        name = "a"
        namespace = "derivationMethod"
