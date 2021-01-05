from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
