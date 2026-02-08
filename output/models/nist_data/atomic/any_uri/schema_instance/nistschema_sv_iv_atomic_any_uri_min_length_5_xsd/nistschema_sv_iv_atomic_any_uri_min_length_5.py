from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-minLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-minLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "min_length": 63,
        },
    )
