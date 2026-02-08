from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "min_exclusive": XmlPeriod("1970-01"),
        }
    )
