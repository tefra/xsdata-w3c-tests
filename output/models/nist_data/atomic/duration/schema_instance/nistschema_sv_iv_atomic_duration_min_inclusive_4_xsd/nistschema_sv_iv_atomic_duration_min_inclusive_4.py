from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-4-NS"

    value: XmlDuration = field(
        metadata={
            "min_inclusive": XmlDuration("P2024Y01M12DT09H17M54S"),
        }
    )
