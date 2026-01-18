from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDateTimeWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-dateTime-whiteSpace-1-NS"

    value: XmlDateTime = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
