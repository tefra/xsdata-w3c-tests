from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-5-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_exclusive": XmlTime(23, 59, 58, 0),
        }
    )
