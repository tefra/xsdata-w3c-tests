from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-minLength-4-NS"


@dataclass
class NistschemaSvIvListNegativeIntegerMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-minLength-4"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-minLength-4-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=8,
            tokens=True
        )
    )
