from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicBooleanPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-boolean-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"false",
        }
    )
