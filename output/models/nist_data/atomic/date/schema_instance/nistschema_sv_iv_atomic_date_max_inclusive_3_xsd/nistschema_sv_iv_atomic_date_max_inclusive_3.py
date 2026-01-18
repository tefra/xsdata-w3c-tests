from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-3-NS"

    value: XmlDate = field(
        metadata={
            "required": True,
            "max_inclusive": XmlDate(2020, 12, 27),
        }
    )
