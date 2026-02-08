from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "psContents"


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"
        namespace = "psContents"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"
        namespace = "psContents"

    value: XmlDate = field()
