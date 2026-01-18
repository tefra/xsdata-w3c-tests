from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
