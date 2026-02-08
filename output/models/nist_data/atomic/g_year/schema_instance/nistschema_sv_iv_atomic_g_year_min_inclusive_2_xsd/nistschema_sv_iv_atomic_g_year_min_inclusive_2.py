from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"

    value: XmlPeriod = field(
        metadata={
            "min_inclusive": XmlPeriod("2010"),
        }
    )
