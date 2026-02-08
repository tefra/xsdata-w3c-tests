from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-2-NS"

    value: XmlDuration = field(
        metadata={
            "max_inclusive": XmlDuration("P1970Y02M12DT08H03M16S"),
        }
    )
