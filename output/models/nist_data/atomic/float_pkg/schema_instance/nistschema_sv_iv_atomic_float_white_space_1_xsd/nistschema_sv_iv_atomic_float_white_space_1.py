from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-float-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicFloatWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-float-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-float-whiteSpace-1-NS"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
