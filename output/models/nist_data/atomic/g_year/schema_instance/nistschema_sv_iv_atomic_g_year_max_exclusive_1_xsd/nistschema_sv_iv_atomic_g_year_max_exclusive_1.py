from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("1971"),
        }
    )
