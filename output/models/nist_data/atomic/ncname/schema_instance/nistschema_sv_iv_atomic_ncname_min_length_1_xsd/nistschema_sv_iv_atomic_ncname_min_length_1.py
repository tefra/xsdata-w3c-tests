from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-NCName-minLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
        }
    )
