from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    ns_test1_ns_test2_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "ns_test1 ns_test2",
            "max_occurs": 2,
            "process_contents": "skip",
        },
    )


@dataclass
class Date:
    class Meta:
        name = "date"
        namespace = "nsConstraint"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
