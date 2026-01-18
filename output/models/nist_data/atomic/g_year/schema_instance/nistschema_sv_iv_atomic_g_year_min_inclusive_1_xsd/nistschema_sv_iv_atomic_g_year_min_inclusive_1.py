from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-1-NS"

    value: XmlPeriod = field(
        metadata={
            "required": True,
            "min_inclusive": XmlPeriod("1970"),
        }
    )
