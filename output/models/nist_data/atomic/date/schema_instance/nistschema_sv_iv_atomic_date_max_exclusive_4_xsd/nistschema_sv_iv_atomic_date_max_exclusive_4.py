from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-4-NS"

    value: XmlDate = field(
        metadata={
            "required": True,
            "max_exclusive": XmlDate(2027, 10, 13),
        }
    )
