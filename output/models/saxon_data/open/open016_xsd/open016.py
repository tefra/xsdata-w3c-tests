from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[XmlDate] = field(
        default=None,
    )
    evidence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    open_com_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
