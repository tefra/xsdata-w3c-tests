from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-3-NS"

    value: XmlDate = field(
        metadata={
            "min_inclusive": XmlDate(2005, 7, 30),
        }
    )
