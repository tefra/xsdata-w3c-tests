from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_inclusive": XmlPeriod("2014-07"),
        }
    )
