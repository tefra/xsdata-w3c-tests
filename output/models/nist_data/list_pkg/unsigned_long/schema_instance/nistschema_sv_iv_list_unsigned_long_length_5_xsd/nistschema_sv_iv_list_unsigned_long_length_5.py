from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-length-5-NS"


@dataclass
class NistschemaSvIvListUnsignedLongLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-length-5"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-length-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
