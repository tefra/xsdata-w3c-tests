from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-minLength-4-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMinLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-minLength-4"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-minLength-4-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=8,
            tokens=True
        )
    )
