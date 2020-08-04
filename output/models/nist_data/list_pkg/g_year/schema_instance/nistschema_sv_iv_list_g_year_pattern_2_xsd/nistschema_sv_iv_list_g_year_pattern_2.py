from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-2-NS"


@dataclass
class NistschemaSvIvListGYearPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"17\d\d 19\d\d \d\d67 \d\d26 \d\d58 \d\d06 \d\d09",
            tokens=True
        )
    )
