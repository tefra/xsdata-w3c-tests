from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "min_exclusive": XmlTime(2, 57, 29, 0),
        }
    )
