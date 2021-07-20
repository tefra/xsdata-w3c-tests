from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicNamePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-Name-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\i\c{45}",
        }
    )
