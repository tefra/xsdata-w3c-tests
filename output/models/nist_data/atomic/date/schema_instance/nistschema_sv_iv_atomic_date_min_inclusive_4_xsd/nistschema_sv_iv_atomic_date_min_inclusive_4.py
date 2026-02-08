from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-4-NS"

    value: XmlDate = field(
        metadata={
            "min_inclusive": XmlDate(1979, 3, 5),
        }
    )
