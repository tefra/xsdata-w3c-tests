from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass(kw_only=True)
class Title:
    class Meta:
        name = "title"
        namespace = "http://www.w3.org/2001/XMLSchema"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
