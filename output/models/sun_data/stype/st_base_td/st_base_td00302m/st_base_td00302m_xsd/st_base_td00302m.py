from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ST_baseTD"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"
        namespace = "ST_baseTD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 3,
            "pattern": r"b+",
        },
    )
