from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNormalizedStringPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){1}Street\s([A-Z][a-z]{1,20}\s){3},\s[A-Z]{2}\s19099-1858",
        },
    )
