from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 861,
        }
    )
