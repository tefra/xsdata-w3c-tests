from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-maxLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-date-maxLength-5-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
