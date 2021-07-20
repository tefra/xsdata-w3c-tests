from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicNamePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\i\c{31}",
        }
    )
