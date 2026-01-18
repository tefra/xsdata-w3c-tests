from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    value: XmlDuration = field(
        metadata={
            "required": True,
        }
    )
