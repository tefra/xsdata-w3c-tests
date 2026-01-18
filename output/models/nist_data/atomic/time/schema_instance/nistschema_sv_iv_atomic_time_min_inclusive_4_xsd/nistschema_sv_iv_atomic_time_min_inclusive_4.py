from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_inclusive": XmlTime(19, 31, 35, 0),
        }
    )
