from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_inclusive": XmlTime(21, 11, 44, 0),
        }
    )
