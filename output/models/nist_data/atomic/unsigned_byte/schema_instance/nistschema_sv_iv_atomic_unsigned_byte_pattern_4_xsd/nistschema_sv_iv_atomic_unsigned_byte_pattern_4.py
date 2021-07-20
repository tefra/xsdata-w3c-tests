from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedBytePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"\d{1}",
        }
    )
