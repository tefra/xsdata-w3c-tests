from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

__NAMESPACE__ = "http://cta023.com/ns"


@dataclass(kw_only=True)
class When:
    class Meta:
        name = "when"
        namespace = "http://cta023.com/ns"

    value: XmlDate | XmlTime | XmlDateTime | XmlPeriod = field()


@dataclass(kw_only=True)
class Event:
    class Meta:
        name = "event"
        namespace = "http://cta023.com/ns"

    when: When = field(
        metadata={
            "type": "Element",
        }
    )
    type_value: None | str = field(
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
        namespace = "http://cta023.com/ns"

    event: list[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
