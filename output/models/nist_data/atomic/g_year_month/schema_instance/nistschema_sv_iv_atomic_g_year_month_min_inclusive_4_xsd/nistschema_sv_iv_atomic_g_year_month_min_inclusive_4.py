from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-4-NS"

    value: XmlPeriod = field(
        metadata={
            "min_inclusive": XmlPeriod("1988-05"),
        }
    )
