from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ST_final"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_final"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
