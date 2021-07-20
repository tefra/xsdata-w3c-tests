from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicTokenPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-token-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\s([A-Z][a-z]{1,20}\s){3},\s[A-Z]{2}\s13653",
        }
    )
