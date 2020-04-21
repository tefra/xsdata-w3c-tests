from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{5}"
        )
    )
