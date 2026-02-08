from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-3-NS"

    value: XmlDateTime = field(
        metadata={
            "min_inclusive": XmlDateTime(1978, 11, 30, 10, 14, 33),
        }
    )
