from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    code: XmlDate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
