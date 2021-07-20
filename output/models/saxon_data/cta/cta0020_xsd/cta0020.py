from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime


@dataclass
class Event:
    class Meta:
        name = "event"

    when: Optional[Union[XmlDate, XmlTime, XmlDateTime, XmlPeriod]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class When:
    class Meta:
        name = "when"

    value: Optional[Union[XmlDate, XmlTime, XmlDateTime, XmlPeriod]] = field(
        default=None
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    event: List[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
