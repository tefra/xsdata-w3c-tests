from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=27948.0
        )
    )