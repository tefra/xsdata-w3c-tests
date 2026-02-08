from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"

    value: XmlTime = field(
        metadata={
            "max_exclusive": XmlTime(8, 19, 11, 0),
        }
    )
