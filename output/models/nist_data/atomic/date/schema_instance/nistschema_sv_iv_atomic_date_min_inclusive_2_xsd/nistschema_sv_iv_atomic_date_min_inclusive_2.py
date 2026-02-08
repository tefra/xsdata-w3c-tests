from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-2-NS"

    value: XmlDate = field(
        metadata={
            "min_inclusive": XmlDate(1973, 9, 8),
        }
    )
