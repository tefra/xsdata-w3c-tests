from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate


@dataclass
class DatedEvent:
    class Meta:
        name = "datedEvent"

    d: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
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
