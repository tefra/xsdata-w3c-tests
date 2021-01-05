from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime


@dataclass
class Doc:
    class Meta:
        name = "doc"

    target: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    equiv: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
