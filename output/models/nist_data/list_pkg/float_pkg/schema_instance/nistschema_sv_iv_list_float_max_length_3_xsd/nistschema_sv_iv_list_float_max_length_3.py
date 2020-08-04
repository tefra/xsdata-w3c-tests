from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-maxLength-3-NS"


@dataclass
class NistschemaSvIvListFloatMaxLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-float-maxLength-3-NS"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=7,
            tokens=True
        )
    )
