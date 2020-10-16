from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-3-NS"


@dataclass
class NistschemaSvIvListHexBinaryMinLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
