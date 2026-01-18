from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-4-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_exclusive": XmlPeriod("--04"),
        }
    )
