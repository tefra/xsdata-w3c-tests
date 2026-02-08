from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"

    value: XmlDuration = field(
        metadata={
            "min_inclusive": XmlDuration("P1978Y12M21DT17H22M44S"),
        }
    )
