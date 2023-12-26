from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
