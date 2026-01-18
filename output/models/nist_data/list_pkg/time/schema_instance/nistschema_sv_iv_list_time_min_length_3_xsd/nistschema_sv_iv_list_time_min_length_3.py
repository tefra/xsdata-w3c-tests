from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListTimeMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-3"
        namespace = "NISTSchema-SV-IV-list-time-minLength-3-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
