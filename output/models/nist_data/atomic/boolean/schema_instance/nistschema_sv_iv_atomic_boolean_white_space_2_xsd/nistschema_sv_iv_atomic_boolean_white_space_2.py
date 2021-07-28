from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2-NS"


@dataclass
class NistschemaSvIvAtomicBooleanWhiteSpace2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-2-NS"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
