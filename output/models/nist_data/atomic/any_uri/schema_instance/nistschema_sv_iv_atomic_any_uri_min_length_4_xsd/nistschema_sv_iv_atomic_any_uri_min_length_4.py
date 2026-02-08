from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-minLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-minLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "min_length": 50,
        },
    )
