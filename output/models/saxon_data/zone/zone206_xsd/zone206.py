from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    target: XmlTime = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    equiv: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
