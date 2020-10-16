from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDurationMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-duration-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-duration-maxLength-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 5,
            "tokens": True,
        }
    )
