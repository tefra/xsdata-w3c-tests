from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-1-NS"

    value: XmlDuration = field(
        metadata={
            "min_inclusive": XmlDuration("P1970Y01M01DT00H00M00S"),
        }
    )
