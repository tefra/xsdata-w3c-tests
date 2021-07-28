from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class DatedEvent:
    class Meta:
        name = "datedEvent"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    event: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Temp(DatedEvent):
    class Meta:
        name = "temp"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    temp: List[Temp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
