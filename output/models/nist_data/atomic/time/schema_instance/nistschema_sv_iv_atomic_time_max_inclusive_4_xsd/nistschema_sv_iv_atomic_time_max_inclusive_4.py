from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"

    value: XmlTime = field(
        metadata={
            "max_inclusive": XmlTime(18, 6, 59, 0),
        }
    )
