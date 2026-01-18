from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-maxLength-3-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
