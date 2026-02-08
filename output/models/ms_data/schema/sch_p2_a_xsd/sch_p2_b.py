from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class BE1:
    class Meta:
        name = "b-e1"
        namespace = "ns-a"

    value: str = field(
        default="",
        metadata={
            "min_length": 4,
        },
    )
