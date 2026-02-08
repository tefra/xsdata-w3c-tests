from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"

    value: XmlTime = field(
        metadata={
            "min_exclusive": XmlTime(13, 38, 10, 0),
        }
    )
