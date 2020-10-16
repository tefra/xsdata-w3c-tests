from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-pattern-5-NS"


@dataclass
class NistschemaSvIvListShortPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-short-pattern-5"
        namespace = "NISTSchema-SV-IV-list-short-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{5} \-\d{4} \-\d{3} \-\d{2} \-\d{1} \d{1} \d{5}",
            "tokens": True,
        }
    )
