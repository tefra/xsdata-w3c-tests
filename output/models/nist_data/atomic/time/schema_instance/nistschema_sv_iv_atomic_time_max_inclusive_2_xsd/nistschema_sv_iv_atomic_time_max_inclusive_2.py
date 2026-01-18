from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-2-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "max_inclusive": XmlTime(13, 46, 8, 0),
        }
    )
