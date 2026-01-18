from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Bar:
    class Meta:
        name = "bar"


@dataclass(kw_only=True)
class Root(Bar):
    class Meta:
        name = "root"
