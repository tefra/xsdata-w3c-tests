from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicStringPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-string-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\n([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s12848",
        }
    )
