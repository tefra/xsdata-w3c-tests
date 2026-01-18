from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-5-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "max_exclusive": XmlTime(23, 59, 59, 0),
        }
    )
