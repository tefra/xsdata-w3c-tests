from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-3-NS"


@dataclass
class NistschemaSvIvListGYearPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d\d93 \d\d27 18\d\d \d\d15 19\d\d \d\d57 18\d\d 19\d\d \d\d57",
            tokens=True
        )
    )
