from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"

    value: XmlTime = field(
        metadata={
            "min_exclusive": XmlTime(0, 0, 0, 0),
        }
    )
