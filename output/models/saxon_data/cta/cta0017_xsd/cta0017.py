from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime


@dataclass
class When:
    class Meta:
        name = "when"

    value: Optional[Union[XmlDate, XmlTime, XmlDateTime, XmlPeriod]] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Event:
    class Meta:
        name = "event"

    when: Optional[When] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
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
    type_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
