from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-maxLength-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicTokenMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-token-maxLength-5-NS"

    value: str = field(
        default="",
        metadata={
            "max_length": 1000,
        },
    )
