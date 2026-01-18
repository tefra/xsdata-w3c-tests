from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class Alpha:
    class Meta:
        name = "alpha"
