from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=3.2371283896903692e+16
        )
    )