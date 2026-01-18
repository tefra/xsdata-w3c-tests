from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListTimeLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-1"
        namespace = "NISTSchema-SV-IV-list-time-length-1-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
