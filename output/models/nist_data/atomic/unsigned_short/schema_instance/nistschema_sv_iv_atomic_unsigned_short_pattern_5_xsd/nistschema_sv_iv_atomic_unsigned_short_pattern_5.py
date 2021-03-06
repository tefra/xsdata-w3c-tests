from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d{5}",
        }
    )
