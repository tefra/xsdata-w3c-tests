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
            "min_inclusive": XmlDuration("-P3D"),
            "max_inclusive": XmlDuration("P3D"),
        }
    )
