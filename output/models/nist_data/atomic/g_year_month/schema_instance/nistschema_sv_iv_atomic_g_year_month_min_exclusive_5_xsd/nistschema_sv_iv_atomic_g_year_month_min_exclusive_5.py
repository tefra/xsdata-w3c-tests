from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"

    value: XmlPeriod = field(
        metadata={
            "min_exclusive": XmlPeriod("2030-11"),
        }
    )
