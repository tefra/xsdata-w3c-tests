from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-4-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){1}Street\s([A-Z][a-z]{1,20}\s){1},\s[A-Z]{2}\s17076",
        },
    )
