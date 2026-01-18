from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-2-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("2030-01"),
        }
    )
