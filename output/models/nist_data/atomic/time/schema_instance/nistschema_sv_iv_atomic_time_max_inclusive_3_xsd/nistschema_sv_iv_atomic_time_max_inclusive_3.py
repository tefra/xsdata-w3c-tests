from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "max_inclusive": XmlTime(5, 7, 34, 0),
        }
    )
