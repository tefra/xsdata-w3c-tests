from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "zot"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "zot"

    value: str = field(default="")


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        namespace = "zot"

    value: str = field(default="")


@dataclass(kw_only=True)
class C:
    class Meta:
        name = "c"
        namespace = "zot"

    value: str = field(default="")
