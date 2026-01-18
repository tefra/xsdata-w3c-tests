from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-length-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListTokenLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-length-1"
        namespace = "NISTSchema-SV-IV-list-token-length-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
