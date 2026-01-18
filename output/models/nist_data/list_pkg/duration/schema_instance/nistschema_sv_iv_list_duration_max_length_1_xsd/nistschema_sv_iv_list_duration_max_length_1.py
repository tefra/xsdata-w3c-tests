from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDurationMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        },
    )
