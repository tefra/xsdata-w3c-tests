from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListTimeMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-5"
        namespace = "NISTSchema-SV-IV-list-time-minLength-5-NS"

    value: list[XmlTime] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
