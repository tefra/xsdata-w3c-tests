from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-pattern-1-NS"


@dataclass
class NistschemaSvIvListDatePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-date-pattern-1"
        namespace = "NISTSchema-SV-IV-list-date-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"19\d\d-\d9-\d4 \d\d40-\d7-1\d 18\d\d-0\d-1\d \d\d05-\d4-\d5 \d\d91-0\d-2\d \d\d84-\d7-\d6 \d\d01-\d0-\d2 19\d\d-\d2-\d7 \d\d87-0\d-1\d",
            "tokens": True,
        }
    )
