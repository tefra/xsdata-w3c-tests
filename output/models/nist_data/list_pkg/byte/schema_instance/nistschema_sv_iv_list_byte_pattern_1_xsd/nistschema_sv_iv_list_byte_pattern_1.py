from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-pattern-1-NS"


@dataclass
class NistschemaSvIvListBytePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-pattern-1"
        namespace = "NISTSchema-SV-IV-list-byte-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\-\d{3} \-\d{2} \-\d{1} \d{1} \d{2} \d{3}",
            tokens=True
        )
    )
