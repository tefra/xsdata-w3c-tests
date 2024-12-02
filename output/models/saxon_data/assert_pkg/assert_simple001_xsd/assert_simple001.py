from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate


@dataclass
class Date:
    class Meta:
        name = "date"

    value: Optional[XmlDate] = field(default=None)


@dataclass
class Outer:
    class Meta:
        name = "outer"

    date: list[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
