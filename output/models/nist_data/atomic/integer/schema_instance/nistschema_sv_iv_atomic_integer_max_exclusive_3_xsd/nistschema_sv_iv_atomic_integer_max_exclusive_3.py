from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=5.49869808681549e+17
        )
    )
