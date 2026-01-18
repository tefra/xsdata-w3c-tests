from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\s([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s11352",
        },
    )
