from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Base:
    class Meta:
        name = "base"

    value: int = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Derived(Base):
    class Meta:
        name = "derived"


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    inner: list[Derived] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
