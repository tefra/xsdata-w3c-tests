from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\.\d{13}",
        }
    )