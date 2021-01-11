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
            "min_inclusive": XmlDateTime(0, 1, 1, 12, 0, 0),
        }
    )
