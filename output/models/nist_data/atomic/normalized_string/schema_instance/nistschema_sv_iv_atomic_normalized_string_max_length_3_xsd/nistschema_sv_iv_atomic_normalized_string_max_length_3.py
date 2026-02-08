from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-3-NS"

    value: str = field(
        default="",
        metadata={
            "max_length": 295,
        },
    )
