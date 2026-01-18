from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-2-NS"

    value: XmlDate = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDate(2016, 9, 5),
        }
    )
