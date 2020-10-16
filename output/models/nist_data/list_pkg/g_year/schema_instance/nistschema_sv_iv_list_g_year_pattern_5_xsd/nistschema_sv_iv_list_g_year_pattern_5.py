from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-5-NS"


@dataclass
class NistschemaSvIvListGYearPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"18\d\d \d\d52 \d\d14 20\d\d \d\d14 \d\d43 \d\d70 19\d\d \d\d36",
            "tokens": True,
        }
    )
