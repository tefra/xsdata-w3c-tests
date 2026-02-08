from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "nsConstraint"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    other_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "process_contents": "skip",
        },
    )


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"
        namespace = "nsConstraint"

    value: XmlDate = field()
