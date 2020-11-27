from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-maxLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 64,
        }
    )
