from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicNormalizedStringMaxLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-normalizedString-maxLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 861,
        }
    )
