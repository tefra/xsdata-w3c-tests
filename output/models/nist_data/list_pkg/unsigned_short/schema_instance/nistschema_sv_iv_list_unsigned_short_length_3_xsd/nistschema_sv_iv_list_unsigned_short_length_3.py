from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-length-3-NS"


@dataclass
class NistschemaSvIvListUnsignedShortLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-length-3"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-length-3-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )
