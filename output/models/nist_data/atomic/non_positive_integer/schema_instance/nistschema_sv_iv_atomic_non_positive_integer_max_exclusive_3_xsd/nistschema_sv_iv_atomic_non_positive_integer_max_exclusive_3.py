from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=-6.411695396315076e+16
        )
    )