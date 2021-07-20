from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-length-3-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-length-3"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-length-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 916,
        }
    )
