from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4-NS"


@dataclass
class NistschemaSvIvAtomicBooleanWhiteSpace4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-4-NS"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
