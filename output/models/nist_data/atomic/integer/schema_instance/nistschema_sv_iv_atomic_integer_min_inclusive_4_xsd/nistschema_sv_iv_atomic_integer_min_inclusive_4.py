from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-integer-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=-1.836402639358703e+17
        )
    )