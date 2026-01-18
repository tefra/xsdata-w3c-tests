from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5-NS"

    value: XmlDuration = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDuration("P2030Y12M31DT23H59M59S"),
        }
    )
