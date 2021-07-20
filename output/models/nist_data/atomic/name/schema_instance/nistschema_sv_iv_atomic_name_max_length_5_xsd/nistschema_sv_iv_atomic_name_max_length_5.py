from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNameMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-maxLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 64,
        }
    )
