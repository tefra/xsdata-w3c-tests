from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNmtokenMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-2-NS"

    value: str = field(
        default="",
        metadata={
            "min_length": 45,
        },
    )
