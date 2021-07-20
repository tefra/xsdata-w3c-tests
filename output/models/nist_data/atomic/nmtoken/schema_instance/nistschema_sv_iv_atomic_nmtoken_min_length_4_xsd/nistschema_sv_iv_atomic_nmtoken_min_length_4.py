from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-minLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 33,
        }
    )
