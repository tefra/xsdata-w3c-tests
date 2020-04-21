from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-length-2-NS"


@dataclass
class NistschemaSvIvListUnsignedShortLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-length-2"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-length-2-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            length=6
        )
    )
