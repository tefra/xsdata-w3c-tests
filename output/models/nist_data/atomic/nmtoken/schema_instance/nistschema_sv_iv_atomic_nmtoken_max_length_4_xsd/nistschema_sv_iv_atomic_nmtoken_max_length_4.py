from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 54,
        }
    )
