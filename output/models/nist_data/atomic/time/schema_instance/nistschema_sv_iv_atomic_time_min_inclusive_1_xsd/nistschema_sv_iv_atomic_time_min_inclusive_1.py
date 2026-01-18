from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-1-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_inclusive": XmlTime(0, 0, 0, 0),
        }
    )
