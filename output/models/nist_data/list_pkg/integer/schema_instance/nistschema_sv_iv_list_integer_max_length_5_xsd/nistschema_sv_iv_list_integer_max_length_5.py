from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-maxLength-5-NS"


@dataclass
class NistschemaSvIvListIntegerMaxLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-integer-maxLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            max_length=10,
            tokens=True
        )
    )
