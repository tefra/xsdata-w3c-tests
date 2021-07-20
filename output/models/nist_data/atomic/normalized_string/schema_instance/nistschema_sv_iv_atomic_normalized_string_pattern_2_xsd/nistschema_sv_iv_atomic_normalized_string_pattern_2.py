from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\s([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s11352",
        }
    )
