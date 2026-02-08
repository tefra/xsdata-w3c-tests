from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: XmlDateTime = field(
        metadata={
            "min_inclusive": XmlDateTime(2000, 1, 1, 0, 0, 0, 0, 0),
            "max_inclusive": XmlDateTime(2999, 12, 31, 23, 59, 59, 0, 0),
        }
    )
