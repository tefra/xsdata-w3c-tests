from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Foo123:
    class Meta:
        name = "foo123"


@dataclass(kw_only=True)
class Root(Foo123):
    class Meta:
        name = "root"
