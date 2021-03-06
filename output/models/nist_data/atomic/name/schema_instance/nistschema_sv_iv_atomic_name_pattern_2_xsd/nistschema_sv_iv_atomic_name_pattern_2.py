from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicNamePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-Name-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\i\c{52}",
        }
    )
