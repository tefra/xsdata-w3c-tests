from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-length-3-NS"


@dataclass
class NistschemaSvIvListIntLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-int-length-3"
        namespace = "NISTSchema-SV-IV-list-int-length-3-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            length=7,
            tokens=True
        )
    )
