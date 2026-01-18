from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
