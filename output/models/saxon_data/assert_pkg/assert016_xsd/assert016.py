from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class DatedEvent:
    class Meta:
        name = "datedEvent"

    d: XmlDate = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Temp(DatedEvent):
    class Meta:
        name = "temp"


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    temp: list[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
