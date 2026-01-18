from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-4"
        namespace = "NISTSchema-SV-IV-list-date-length-4-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 8,
            "tokens": True,
        },
    )
