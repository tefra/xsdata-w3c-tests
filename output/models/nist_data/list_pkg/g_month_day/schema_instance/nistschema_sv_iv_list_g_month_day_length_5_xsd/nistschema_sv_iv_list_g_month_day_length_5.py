from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthDayLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-length-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-length-5-NS"

    value: list[XmlPeriod] = field(
        default_factory=list,
        metadata={
            "length": 10,
            "tokens": True,
        },
    )
