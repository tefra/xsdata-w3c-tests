from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-minLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1000,
        }
    )
