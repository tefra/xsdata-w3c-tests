from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDateTime(2000, 1, 1, 0, 0, 0, 0, 0),
            "max_inclusive": XmlDateTime(2999, 12, 31, 23, 59, 59, 0, 0),
        },
    )
