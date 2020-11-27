from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDurationMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-minExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "P2030Y12M31DT23H59M58S",
        }
    )
