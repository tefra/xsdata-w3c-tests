from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-3-NS"

    value: XmlDuration = field(
        metadata={
            "min_exclusive": XmlDuration("P2030Y05M22DT14H53M02S"),
        }
    )
