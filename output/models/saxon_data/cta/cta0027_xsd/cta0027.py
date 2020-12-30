from dataclasses import dataclass, field
from datetime import datetime, time
from typing import List, Optional, Union

__NAMESPACE__ = "http://cta023.com/ns"


@dataclass
class Event:
    class Meta:
        name = "event"
        namespace = "http://cta023.com/ns"

    when: Optional[Union[str, time, datetime]] = field(
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
        namespace = "http://cta023.com/ns"

    value: Optional[Union[str, time, datetime]] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://cta023.com/ns"

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
