from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-1-NS"

    value: XmlDate = field(
        metadata={
            "min_exclusive": XmlDate(1970, 1, 1),
        }
    )
