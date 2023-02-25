from dataclasses import dataclass, field
from typing import List
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "targetNS1"


@dataclass
class A1:
    class Meta:
        name = "A"

    c_or_date: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c",
                    "type": int,
                    "namespace": "",
                },
                {
                    "name": "date",
                    "type": XmlDate,
                    "namespace": "",
                },
            ),
            "max_occurs": 2,
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "targetNS1"
