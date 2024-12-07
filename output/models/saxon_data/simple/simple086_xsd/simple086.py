from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration


@dataclass
class Elem:
    class Meta:
        name = "elem"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
