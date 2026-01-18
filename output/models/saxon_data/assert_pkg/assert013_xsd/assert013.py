from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass(kw_only=True)
class DatedEvent:
    class Meta:
        name = "datedEvent"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )
    event: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
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
