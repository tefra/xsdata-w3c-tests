from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    value: XmlDuration = field(
        metadata={
            "min_inclusive": XmlDuration("-P3D"),
            "max_inclusive": XmlDuration("P3D"),
        }
    )
