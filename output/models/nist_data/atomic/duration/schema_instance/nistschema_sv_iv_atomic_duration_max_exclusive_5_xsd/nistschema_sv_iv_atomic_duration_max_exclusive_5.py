from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDurationMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-duration-maxExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": "P2030Y12M31DT23H59M59S",
        }
    )
