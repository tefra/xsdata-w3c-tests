from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{3}"
        )
    )