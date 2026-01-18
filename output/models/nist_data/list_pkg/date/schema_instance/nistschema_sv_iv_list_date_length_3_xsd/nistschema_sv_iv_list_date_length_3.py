from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-length-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-length-3"
        namespace = "NISTSchema-SV-IV-list-date-length-3-NS"

    value: list[XmlDate] = field(
        default_factory=list,
        metadata={
            "length": 7,
            "tokens": True,
        },
    )
