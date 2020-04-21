from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{7}"
        )
    )
