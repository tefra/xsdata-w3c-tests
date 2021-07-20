from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 0,
        }
    )
