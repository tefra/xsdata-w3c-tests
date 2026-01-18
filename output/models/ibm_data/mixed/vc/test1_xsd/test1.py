from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    value: int = field()
