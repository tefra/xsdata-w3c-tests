from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-2-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_inclusive": XmlPeriod("--09"),
        }
    )
