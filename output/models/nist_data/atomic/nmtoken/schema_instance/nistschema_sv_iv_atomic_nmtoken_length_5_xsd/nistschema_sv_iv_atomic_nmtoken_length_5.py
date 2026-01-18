from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-length-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNmtokenLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-length-5"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-length-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "length": 64,
        },
    )
