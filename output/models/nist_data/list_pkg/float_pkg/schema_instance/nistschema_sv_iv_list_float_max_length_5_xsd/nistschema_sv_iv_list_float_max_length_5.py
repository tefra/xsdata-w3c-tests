from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-maxLength-5-NS"


@dataclass
class NistschemaSvIvListFloatMaxLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-float-maxLength-5-NS"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            max_length=10.0
        )
    )