from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-5-NS"

    value: XmlDateTime = field(
        metadata={
            "max_inclusive": XmlDateTime(2030, 12, 31, 23, 59, 59),
        }
    )
