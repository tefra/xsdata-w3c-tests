from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_inclusive": XmlTime(1, 3, 8, 0),
        }
    )
