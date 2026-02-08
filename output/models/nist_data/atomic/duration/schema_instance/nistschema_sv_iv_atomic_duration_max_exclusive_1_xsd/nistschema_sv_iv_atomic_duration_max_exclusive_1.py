from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-1-NS"

    value: XmlDuration = field(
        metadata={
            "max_exclusive": XmlDuration("P1970Y01M01DT00H00M01S"),
        }
    )
