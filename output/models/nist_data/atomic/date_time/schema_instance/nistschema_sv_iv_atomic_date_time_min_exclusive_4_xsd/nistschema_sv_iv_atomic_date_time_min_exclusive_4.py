from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-4-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "min_exclusive": XmlDateTime(2001, 9, 4, 0, 13, 18),
        }
    )
