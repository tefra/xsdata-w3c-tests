from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-5-NS"

    value: XmlDateTime = field(
        metadata={
            "min_exclusive": XmlDateTime(2030, 12, 31, 23, 59, 58),
        }
    )
