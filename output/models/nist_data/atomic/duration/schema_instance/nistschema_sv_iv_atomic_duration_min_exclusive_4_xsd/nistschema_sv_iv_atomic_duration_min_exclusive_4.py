from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-4-NS"

    value: XmlDuration = field(
        metadata={
            "min_exclusive": XmlDuration("P2029Y10M29DT21H06M18S"),
        }
    )
