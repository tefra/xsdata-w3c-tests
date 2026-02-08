from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"

    value: XmlDate = field(
        metadata={
            "max_exclusive": XmlDate(2030, 12, 31),
        }
    )
