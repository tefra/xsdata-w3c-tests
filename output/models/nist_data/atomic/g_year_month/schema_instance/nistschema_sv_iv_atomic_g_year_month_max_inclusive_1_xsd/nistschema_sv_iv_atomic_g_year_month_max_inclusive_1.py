from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_inclusive": XmlPeriod("1970-01"),
        }
    )
