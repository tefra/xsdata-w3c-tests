from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"--\d9",
        }
    )
