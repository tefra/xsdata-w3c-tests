from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://assert020.ns/"


@dataclass(kw_only=True)
class Temp:
    class Meta:
        name = "temp"
        namespace = "http://assert020.ns/"

    temp: list[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
