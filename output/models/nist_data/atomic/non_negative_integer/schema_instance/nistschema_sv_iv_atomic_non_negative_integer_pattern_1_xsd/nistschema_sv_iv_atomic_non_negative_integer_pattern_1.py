from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{1}",
        }
    )
