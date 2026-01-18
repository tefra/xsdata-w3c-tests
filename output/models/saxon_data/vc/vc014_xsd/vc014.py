from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Temp:
    class Meta:
        name = "temp"

    x: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
