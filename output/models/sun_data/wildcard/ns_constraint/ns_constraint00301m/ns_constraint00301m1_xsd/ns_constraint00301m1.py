from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "nsConstraint"


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"
        namespace = "nsConstraint"

    value: XmlDate = field(
        metadata={
            "required": True,
        }
    )
