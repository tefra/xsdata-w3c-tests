from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minInclusive-3-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("--07"),
        }
    )
