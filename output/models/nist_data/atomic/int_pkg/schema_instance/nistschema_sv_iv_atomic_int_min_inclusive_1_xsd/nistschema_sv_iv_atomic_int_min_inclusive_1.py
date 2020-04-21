from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicIntMinInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=-2147483648.0
        )
    )
