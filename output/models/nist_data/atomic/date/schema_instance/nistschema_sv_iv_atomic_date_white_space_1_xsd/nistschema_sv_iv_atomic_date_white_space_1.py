from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-date-whiteSpace-1-NS"

    value: XmlDate = field(
        metadata={
            "white_space": "collapse",
        }
    )
