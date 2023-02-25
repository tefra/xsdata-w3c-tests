from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "particles"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "particles"

    date_or_marked: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
                {
                    "name": "marked",
                    "type": bool,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )
    num: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
