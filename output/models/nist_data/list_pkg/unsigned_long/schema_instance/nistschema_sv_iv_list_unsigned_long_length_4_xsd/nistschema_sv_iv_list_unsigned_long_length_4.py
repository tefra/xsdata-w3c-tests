from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-length-4-NS"


@dataclass
class NistschemaSvIvListUnsignedLongLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-length-4"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-length-4-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
