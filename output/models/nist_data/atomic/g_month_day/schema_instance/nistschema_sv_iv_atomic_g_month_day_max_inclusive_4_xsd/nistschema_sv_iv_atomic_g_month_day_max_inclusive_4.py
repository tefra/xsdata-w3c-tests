from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthDayMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"

    value: XmlPeriod = field(
        metadata={
            "max_inclusive": XmlPeriod("--07-01"),
        }
    )
