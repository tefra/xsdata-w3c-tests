from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: XmlDateTime = field(
        metadata={
            "required": True,
        }
    )
