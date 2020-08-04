from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-length-4-NS"


@dataclass
class NistschemaSvIvListFloatLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-float-length-4"
        namespace = "NISTSchema-SV-IV-list-float-length-4-NS"

    value: List[float] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            length=8,
            tokens=True
        )
    )
