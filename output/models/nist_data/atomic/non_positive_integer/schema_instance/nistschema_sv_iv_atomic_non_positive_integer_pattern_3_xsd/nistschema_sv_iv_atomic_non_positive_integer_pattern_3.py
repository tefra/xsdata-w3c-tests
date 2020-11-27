from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\d{9}",
        }
    )
