from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": XmlDuration("-P3Y"),
            "max_inclusive": XmlDuration("P3Y"),
        }
    )
