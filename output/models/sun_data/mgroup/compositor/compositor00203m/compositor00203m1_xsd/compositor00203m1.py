from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "compositor"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "compositor"
