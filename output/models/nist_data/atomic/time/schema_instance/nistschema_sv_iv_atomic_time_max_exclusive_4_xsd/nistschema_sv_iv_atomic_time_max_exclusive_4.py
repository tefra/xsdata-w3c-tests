from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "max_exclusive": XmlTime(12, 25, 37, 0),
        }
    )
