from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime


@dataclass(kw_only=True)
class When:
    class Meta:
        name = "when"

    value: XmlDate | XmlTime | XmlDateTime | XmlPeriod = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Event:
    class Meta:
        name = "event"

    when: When = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_value: None | object = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    event: list[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    type_value: None | object = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
