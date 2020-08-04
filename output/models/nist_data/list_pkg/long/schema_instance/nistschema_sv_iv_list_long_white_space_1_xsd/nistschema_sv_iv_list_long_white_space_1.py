from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListLongWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-long-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-long-whiteSpace-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            white_space="collapse",
            tokens=True
        )
    )
