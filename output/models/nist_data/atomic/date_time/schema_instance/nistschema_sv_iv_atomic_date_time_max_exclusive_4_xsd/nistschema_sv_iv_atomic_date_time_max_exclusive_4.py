from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-maxExclusive-4-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDateTime(2018, 6, 17, 15, 34, 43),
        }
    )
