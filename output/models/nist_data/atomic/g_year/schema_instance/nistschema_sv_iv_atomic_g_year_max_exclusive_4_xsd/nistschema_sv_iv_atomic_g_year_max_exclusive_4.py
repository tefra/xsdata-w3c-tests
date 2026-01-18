from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-4-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("2005"),
        }
    )
