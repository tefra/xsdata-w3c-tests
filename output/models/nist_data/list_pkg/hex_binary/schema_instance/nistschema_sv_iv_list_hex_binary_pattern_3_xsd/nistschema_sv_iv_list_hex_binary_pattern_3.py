from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-3-NS"


@dataclass
class NistschemaSvIvListHexBinaryPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"[0-9A-F]{42} [0-9A-F]{32} [0-9A-F]{2} [0-9A-F]{34} [0-9A-F]{68}"
        )
    )