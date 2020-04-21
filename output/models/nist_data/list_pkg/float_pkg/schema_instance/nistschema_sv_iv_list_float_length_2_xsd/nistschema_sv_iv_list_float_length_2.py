from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-length-2-NS"


@dataclass
class NistschemaSvIvListFloatLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-length-2"
        namespace = "NISTSchema-SV-IV-list-float-length-2-NS"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            length=6
        )
    )
