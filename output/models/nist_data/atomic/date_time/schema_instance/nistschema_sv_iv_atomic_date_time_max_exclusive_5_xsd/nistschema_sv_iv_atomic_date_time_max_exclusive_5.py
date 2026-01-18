from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-5-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDateTime(2030, 12, 31, 23, 59, 59),
        }
    )
