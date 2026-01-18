from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-minLength-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-minLength-4-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 74,
        },
    )
