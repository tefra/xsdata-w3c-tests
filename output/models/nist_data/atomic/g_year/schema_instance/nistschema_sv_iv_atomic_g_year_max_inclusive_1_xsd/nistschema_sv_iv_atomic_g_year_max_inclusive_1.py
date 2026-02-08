from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "max_inclusive": XmlPeriod("1970"),
        }
    )
