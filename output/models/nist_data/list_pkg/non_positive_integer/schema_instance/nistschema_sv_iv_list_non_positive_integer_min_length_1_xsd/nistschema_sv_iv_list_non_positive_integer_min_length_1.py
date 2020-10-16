from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-minLength-1-NS"


@dataclass
class NistschemaSvIvListNonPositiveIntegerMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-minLength-1"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-minLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 5,
            "tokens": True,
        }
    )
