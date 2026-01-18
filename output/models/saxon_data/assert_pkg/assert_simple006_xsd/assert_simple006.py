from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass(kw_only=True)
class Value:
    class Meta:
        name = "value"

    value: XmlDate | XmlDateTime = field()


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    value: list[Value] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
