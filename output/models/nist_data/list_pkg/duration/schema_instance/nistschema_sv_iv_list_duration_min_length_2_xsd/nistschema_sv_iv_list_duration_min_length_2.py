from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDurationMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-minLength-2"
        namespace = "NISTSchema-SV-IV-list-duration-minLength-2-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        },
    )
