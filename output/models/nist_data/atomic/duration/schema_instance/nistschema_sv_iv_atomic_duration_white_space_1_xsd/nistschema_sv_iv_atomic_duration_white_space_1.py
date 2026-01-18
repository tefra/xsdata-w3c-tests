from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDurationWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-duration-whiteSpace-1-NS"

    value: XmlDuration = field(
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
