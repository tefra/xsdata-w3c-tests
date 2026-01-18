from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-5"
        namespace = "NISTSchema-SV-IV-list-date-length-5-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
