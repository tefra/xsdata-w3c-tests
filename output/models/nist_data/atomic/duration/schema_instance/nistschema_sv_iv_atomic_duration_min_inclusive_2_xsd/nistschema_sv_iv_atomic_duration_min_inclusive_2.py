from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-duration-minInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="P1978Y12M21DT17H22M44S"
        )
    )
