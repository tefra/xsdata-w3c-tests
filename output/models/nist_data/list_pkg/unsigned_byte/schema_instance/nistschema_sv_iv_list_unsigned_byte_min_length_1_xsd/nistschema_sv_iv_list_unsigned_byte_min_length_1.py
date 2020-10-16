from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-minLength-1-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-minLength-1"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-minLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 5,
            "tokens": True,
        }
    )
