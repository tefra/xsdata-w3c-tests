from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){1}Street\s([A-Z][a-z]{1,20}\s){3},\s[A-Z]{2}\s19099-1858",
        }
    )
