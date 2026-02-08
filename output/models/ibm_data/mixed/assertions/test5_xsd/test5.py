from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Value:
    class Meta:
        name = "value"

    value: str = field(default="")
