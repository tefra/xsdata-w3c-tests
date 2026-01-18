from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-time-whiteSpace-1-NS"

    value: XmlTime = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
