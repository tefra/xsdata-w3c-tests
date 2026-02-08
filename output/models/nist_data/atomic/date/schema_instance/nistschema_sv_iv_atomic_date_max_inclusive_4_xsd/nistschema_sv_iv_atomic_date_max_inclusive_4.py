from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"

    value: XmlDate = field(
        metadata={
            "max_inclusive": XmlDate(1971, 1, 23),
        }
    )
