from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedBytePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"\d{2}"
        )
    )