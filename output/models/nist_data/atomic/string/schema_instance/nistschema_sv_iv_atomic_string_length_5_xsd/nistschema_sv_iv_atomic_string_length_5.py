from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-string-length-5-NS"


@dataclass
class NistschemaSvIvAtomicStringLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-string-length-5"
        namespace = "NISTSchema-SV-IV-atomic-string-length-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 1000,
        }
    )
