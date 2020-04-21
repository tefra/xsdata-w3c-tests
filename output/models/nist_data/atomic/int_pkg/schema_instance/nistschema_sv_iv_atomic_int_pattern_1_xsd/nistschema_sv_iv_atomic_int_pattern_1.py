from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicIntPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-int-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\-\d{10}"
        )
    )
