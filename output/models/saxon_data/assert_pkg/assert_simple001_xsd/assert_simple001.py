from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Date:
    class Meta:
        name = "date"

    value: XmlDate = field()


@dataclass(kw_only=True)
class Outer:
    class Meta:
        name = "outer"

    date: list[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
