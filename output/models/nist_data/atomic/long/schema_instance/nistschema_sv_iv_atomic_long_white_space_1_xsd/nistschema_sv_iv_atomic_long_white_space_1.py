from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicLongWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-long-whiteSpace-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "white_space": "collapse",
        }
    )
