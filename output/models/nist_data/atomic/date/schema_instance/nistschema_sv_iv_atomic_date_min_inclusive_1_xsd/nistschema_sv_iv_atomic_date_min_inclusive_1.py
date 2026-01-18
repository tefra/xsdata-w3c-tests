from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"

    value: XmlDate = field(
        metadata={
            "required": True,
            "min_inclusive": XmlDate(1970, 1, 1),
        }
    )
