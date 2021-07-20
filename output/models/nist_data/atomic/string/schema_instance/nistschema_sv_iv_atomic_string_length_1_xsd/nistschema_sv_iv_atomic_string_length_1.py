from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-length-1-NS"


@dataclass
class NistschemaSvIvAtomicStringLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-length-1"
        namespace = "NISTSchema-SV-IV-atomic-string-length-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 0,
        }
    )
