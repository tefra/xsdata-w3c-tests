from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"--\d6",
        }
    )
