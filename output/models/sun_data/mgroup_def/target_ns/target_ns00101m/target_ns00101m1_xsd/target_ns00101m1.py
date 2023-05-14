from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "targetNS0"


@dataclass
class A1:
    class Meta:
        name = "A"

    c_or_date: Optional[object] = field(
        default=None,
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
        }
    )


@dataclass
class A(A1):
    class Meta:
        name = "a"
        namespace = "targetNS0"
