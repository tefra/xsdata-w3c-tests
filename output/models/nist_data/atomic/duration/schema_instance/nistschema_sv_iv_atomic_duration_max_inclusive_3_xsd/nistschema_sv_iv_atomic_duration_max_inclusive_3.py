from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxInclusive-3-NS"

    value: XmlDuration = field(
        metadata={
            "required": True,
            "max_inclusive": XmlDuration("P1981Y03M20DT22H33M14S"),
        }
    )
