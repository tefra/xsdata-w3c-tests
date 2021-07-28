from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 42,
        }
    )
