from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-2-NS"

    value: XmlDuration = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDuration("P1990Y06M11DT15H00M05S"),
        }
    )
