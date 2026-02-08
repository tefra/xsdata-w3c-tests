from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    value: str = field(default="")


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
