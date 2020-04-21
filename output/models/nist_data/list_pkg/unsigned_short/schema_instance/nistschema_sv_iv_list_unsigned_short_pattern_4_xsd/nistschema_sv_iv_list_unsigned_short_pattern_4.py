from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedShort-pattern-4-NS"


@dataclass
class NistschemaSvIvListUnsignedShortPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedShort-pattern-4"
        namespace = "NISTSchema-SV-IV-list-unsignedShort-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d{1} \d{2} \d{3} \d{4} \d{5} \d{1}"
        )
    )
