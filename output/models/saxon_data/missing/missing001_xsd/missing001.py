from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Bad:
    class Meta:
        name = "bad"


@dataclass(kw_only=True)
class Good:
    class Meta:
        name = "good"

    value: int = field()
