from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "explicit_timezone": "optional",
        }
    )
