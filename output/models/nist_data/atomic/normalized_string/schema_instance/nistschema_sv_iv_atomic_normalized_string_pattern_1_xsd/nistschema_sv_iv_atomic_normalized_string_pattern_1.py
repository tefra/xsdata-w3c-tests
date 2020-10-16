from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\s([A-Z][a-z]{1,20}\s){1},\s[A-Z]{2}\s18037",
        }
    )
