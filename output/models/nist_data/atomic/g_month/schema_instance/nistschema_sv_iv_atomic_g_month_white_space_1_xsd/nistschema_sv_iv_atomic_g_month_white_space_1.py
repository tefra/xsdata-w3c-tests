from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-whiteSpace-1-NS"

    value: XmlPeriod = field(
        metadata={
            "white_space": "collapse",
        }
    )
