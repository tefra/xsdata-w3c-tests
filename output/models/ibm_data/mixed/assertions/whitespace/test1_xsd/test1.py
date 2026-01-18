from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class X:
    class Meta:
        name = "x"

    value: int = field()
