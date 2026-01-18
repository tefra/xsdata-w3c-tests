from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\s([A-Z][a-z]{1,20}\s){3},\s[A-Z]{2}\s12317",
        },
    )
