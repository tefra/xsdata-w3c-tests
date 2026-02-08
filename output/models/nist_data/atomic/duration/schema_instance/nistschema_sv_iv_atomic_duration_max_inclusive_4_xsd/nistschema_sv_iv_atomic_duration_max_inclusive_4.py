from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-4-NS"

    value: XmlDuration = field(
        metadata={
            "max_inclusive": XmlDuration("P1989Y04M21DT11H28M41S"),
        }
    )
