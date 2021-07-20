from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicStringPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-string-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1,5}\s([A-Z][a-z]{1,20}\s){4}Street\n([A-Z][a-z]{1,20}\s){2},\s[A-Z]{2}\s17687",
        }
    )
