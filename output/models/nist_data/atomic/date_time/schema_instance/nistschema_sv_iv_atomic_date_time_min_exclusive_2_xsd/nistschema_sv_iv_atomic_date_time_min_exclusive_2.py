from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-minExclusive-2-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "min_exclusive": XmlDateTime(1974, 4, 26, 23, 23, 51),
        }
    )
