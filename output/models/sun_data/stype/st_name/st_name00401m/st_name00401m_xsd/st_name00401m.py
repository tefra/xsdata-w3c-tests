from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ST_name"


@dataclass(kw_only=True)
class Test:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"1|2|3",
        },
    )
