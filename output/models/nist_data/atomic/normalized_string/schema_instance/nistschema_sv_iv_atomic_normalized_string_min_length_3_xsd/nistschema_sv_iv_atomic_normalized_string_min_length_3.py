from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-minLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 628,
        }
    )
