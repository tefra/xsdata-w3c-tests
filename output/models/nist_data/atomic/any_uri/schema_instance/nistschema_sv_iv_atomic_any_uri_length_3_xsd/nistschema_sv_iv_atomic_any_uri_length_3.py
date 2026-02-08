from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-length-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicAnyUriLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-length-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-length-3-NS"

    value: str = field(
        default="",
        metadata={
            "length": 34,
        },
    )
