from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    target: XmlDuration = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    equiv: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
