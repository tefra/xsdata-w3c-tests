from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=-1810120723.0
        )
    )