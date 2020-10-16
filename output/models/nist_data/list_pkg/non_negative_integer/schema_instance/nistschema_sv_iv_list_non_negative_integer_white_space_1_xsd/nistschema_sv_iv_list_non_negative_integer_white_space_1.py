from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListNonNegativeIntegerWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-whiteSpace-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "white_space": "collapse",
            "tokens": True,
        }
    )
