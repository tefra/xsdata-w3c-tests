from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\d{2}\.\d{3}",
        }
    )
