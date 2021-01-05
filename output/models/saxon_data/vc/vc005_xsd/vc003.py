from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Temp:
    class Meta:
        name = "temp"

    value: Optional[XmlDate] = field(
        default=None,
    )
