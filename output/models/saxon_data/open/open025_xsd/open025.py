from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate


@dataclass
class T:
    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
            "process_contents": "skip",
        },
    )
    i: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    d: List[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Doc(T):
    class Meta:
        name = "doc"
