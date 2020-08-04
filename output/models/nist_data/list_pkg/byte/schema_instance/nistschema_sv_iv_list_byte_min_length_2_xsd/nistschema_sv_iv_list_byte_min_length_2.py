from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-minLength-2-NS"


@dataclass
class NistschemaSvIvListByteMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-minLength-2"
        namespace = "NISTSchema-SV-IV-list-byte-minLength-2-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=6,
            tokens=True
        )
    )
