from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-3-NS"

    value: XmlDuration = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDuration("P2009Y03M30DT15H11M46S"),
        }
    )
