from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxInclusive-4-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "max_inclusive": XmlDateTime(1972, 9, 29, 19, 51, 19),
        }
    )
