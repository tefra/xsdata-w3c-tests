from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-minLength-5-NS"


@dataclass
class NistschemaSvIvListDateMinLength5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-date-minLength-5"
        namespace = "NISTSchema-SV-IV-list-date-minLength-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=10,
            tokens=True
        )
    )
