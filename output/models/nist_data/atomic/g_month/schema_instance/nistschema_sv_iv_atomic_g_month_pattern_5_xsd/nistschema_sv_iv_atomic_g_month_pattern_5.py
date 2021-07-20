from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"--0\d",
        }
    )
