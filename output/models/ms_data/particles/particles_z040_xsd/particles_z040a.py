from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class A1:
    class Meta:
        name = "a1"
        namespace = "a"

    value: str = field(init=False, default="a1")


@dataclass(kw_only=True)
class A2:
    class Meta:
        name = "a2"
        namespace = "a"

    value: str = field(default="a2")
