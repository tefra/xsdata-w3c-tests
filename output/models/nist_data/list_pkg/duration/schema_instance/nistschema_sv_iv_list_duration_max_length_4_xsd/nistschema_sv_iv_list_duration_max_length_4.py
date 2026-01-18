from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDurationMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-4-NS"

    value: list[XmlDuration] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
