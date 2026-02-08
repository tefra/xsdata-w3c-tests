from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    value: str = field(default="")


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
