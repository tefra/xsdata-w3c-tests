from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Temp:
    class Meta:
        name = "temp"

    value: Optional[XmlDate] = field(
        default=None
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Attribute",
            "required": True,
        }
    )
