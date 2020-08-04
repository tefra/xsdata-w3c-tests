from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-maxLength-1-NS"


@dataclass
class NistschemaSvIvListFloatMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-float-maxLength-1-NS"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=5,
            tokens=True
        )
    )
