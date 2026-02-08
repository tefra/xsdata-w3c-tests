from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-2-NS"

    value: XmlDate = field(
        metadata={
            "max_inclusive": XmlDate(2029, 9, 9),
        }
    )
