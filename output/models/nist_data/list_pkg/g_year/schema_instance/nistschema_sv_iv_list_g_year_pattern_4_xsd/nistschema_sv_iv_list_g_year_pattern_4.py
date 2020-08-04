from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-4-NS"


@dataclass
class NistschemaSvIvListGYearPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"19\d\d \d\d48 \d\d53 18\d\d \d\d43 19\d\d \d\d10 \d\d46",
            tokens=True
        )
    )
