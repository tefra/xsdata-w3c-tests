from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-pattern-3-NS"


@dataclass
class NistschemaSvIvListLongPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-long-pattern-3"
        namespace = "NISTSchema-SV-IV-list-long-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\-\d{18} \-\d{9} \-\d{1} \d{5} \d{18}"
        )
    )