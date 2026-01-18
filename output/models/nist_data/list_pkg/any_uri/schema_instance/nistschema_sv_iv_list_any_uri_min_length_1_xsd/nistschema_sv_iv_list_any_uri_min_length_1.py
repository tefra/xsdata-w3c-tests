from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-anyURI-minLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListAnyUriMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-anyURI-minLength-1"
        namespace = "NISTSchema-SV-IV-list-anyURI-minLength-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
