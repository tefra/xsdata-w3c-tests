from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{40}",
        }
    )
