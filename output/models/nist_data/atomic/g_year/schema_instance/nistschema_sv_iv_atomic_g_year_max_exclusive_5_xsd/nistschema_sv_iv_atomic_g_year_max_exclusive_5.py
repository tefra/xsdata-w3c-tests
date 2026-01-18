from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("2030"),
        }
    )
