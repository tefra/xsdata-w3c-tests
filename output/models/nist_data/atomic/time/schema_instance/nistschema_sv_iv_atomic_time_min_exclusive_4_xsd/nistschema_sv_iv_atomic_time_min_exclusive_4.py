from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"

    value: XmlTime = field(
        metadata={
            "min_exclusive": XmlTime(18, 16, 28, 0),
        }
    )
