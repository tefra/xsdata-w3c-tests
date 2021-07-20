from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\-\d{18}",
        }
    )
