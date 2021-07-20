from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicBooleanWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-1-NS"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "white_space": "collapse",
        }
    )
