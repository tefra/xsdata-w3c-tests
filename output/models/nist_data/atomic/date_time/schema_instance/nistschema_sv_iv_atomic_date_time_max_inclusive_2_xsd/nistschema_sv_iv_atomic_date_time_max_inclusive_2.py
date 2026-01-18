from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-2-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "max_inclusive": XmlDateTime(1982, 5, 22, 18, 1, 37),
        }
    )
