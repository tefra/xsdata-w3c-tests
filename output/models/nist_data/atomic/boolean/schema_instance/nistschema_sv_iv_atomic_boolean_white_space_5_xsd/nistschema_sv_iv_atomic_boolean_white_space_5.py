from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"


@dataclass
class NistschemaSvIvAtomicBooleanWhiteSpace5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5"
        namespace = "NISTSchema-SV-IV-atomic-boolean-whiteSpace-5-NS"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        },
    )
