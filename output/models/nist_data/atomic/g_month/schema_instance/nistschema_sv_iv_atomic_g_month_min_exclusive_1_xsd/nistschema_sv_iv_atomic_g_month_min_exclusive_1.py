from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("--01"),
        }
    )
