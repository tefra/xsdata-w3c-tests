from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-3-NS"

    value: XmlPeriod = field(
        metadata={
            "max_inclusive": XmlPeriod("1986-01"),
        }
    )
