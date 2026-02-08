from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-3-NS"

    value: XmlDuration = field(
        metadata={
            "min_inclusive": XmlDuration("P1989Y09M10DT10H34M11S"),
        }
    )
