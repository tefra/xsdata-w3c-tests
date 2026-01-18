from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthDayMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxExclusive-3-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("--07-23"),
        }
    )
