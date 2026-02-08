from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-3-NS"

    value: XmlDateTime = field(
        metadata={
            "min_exclusive": XmlDateTime(1981, 6, 8, 6, 29, 37),
        }
    )
