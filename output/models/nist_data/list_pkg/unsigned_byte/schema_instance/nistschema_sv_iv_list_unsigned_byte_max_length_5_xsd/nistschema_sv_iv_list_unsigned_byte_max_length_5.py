from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-maxLength-5-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMaxLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-maxLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            max_length=10
        )
    )
