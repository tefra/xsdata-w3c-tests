from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-minExclusive-2-NS"

    value: XmlDate = field(
        metadata={
            "required": True,
            "min_exclusive": XmlDate(2027, 3, 5),
        }
    )
