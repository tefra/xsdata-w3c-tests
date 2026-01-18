from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-maxExclusive-2-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "max_exclusive": XmlPeriod("--02"),
        }
    )
