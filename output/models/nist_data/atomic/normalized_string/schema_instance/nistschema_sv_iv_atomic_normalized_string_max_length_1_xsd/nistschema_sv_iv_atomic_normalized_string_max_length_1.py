from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 0,
        },
    )
