from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-4-NS"


@dataclass
class NistschemaSvIvListHexBinaryPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[0-9A-F]{58} [0-9A-F]{62} [0-9A-F]{50} [0-9A-F]{42} [0-9A-F]{18} [0-9A-F]{64} [0-9A-F]{54} [0-9A-F]{20} [0-9A-F]{32} [0-9A-F]{12}"
        )
    )