from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNameMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-Name-maxLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 24,
        }
    )
