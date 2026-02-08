from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-3-NS"

    value: XmlDate = field(
        metadata={
            "min_exclusive": XmlDate(2005, 11, 17),
        }
    )
