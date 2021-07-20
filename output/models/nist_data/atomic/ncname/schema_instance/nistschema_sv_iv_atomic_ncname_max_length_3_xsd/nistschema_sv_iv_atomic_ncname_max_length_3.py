from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NCName-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicNcnameMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NCName-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-NCName-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 12,
        }
    )
