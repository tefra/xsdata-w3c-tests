from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=7.0
        )
    )