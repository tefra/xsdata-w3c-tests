from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthDayMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5-NS"

    value: XmlPeriod = field(
        metadata={
            "min_inclusive": XmlPeriod("--12-31"),
        }
    )
