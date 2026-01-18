from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: XmlTime = field(
        metadata={
            "explicit_timezone": "optional",
        }
    )
