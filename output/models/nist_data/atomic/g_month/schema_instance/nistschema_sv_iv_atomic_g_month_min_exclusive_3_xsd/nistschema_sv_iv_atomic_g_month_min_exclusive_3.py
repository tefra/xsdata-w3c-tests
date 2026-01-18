from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-3-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("--03"),
        }
    )
