from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=-9.112482283251717e+17
        )
    )