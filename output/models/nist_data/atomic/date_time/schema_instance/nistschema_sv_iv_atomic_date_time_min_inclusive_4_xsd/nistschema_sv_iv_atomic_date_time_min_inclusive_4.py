from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minInclusive-4-NS"

    value: XmlDateTime = field(
        metadata={
            "min_inclusive": XmlDateTime(2006, 7, 21, 1, 32, 21),
        }
    )
