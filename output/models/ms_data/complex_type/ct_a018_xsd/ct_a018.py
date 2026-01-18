from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"


@dataclass(kw_only=True)
class Root(Foo):
    class Meta:
        name = "root"
